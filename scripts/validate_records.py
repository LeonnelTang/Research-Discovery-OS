#!/usr/bin/env python3
"""Validate RDOS Markdown record headers and ID relationships without external dependencies.

This intentionally supports only the project's simple YAML-front-matter subset.
It is a structural safeguard, not a scientific/provenance verifier or full YAML parser.
"""
from __future__ import annotations
from datetime import datetime
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'
SCHEMAS = {
    'goals': ('G', 'ResearchGoal', ['id', 'record_type', 'created_at', 'title', 'question', 'status', 'success_criteria', 'constraints']),
    'hypotheses': ('H', 'Hypothesis', ['id', 'record_type', 'created_at', 'goal_id', 'version', 'status', 'claim', 'assumptions', 'predictions', 'falsifiers']),
    'evidence': ('E', 'Evidence', ['id', 'record_type', 'created_at', 'source_type', 'source_ref', 'verification_status', 'observation']),
    'experiments': ('X', 'Experiment', ['id', 'record_type', 'created_at', 'hypothesis_ids', 'status', 'protocol', 'primary_metric', 'controls', 'budget']),
    'decisions': ('D', 'ResearchDecision', ['id', 'record_type', 'created_at', 'goal_id', 'options', 'selected', 'rationale', 'next_action']),
}
VALID_STATUS = {
    'goals': {'ACTIVE','PAUSED','ARCHIVED'},
    'hypotheses': {'PROPOSED','GROUNDED','TESTABLE','QUEUED','TESTING','EVALUATED'},
    'experiments': {'DRAFT','VALIDATED','APPROVED','QUEUED','RUNNING','COMPLETED','FAILED','CANCELLED'},
}
VALID_VERIFICATION = {'unverified','source-reported','reproduced','conflicting','invalidated'}


def frontmatter(content: str) -> dict[str, str]:
    if not content.startswith('---\n'):
        raise ValueError('no starting frontmatter delimiter')
    marker = '\n---\n'
    end = content.find(marker, 4)
    if end < 0:
        raise ValueError('no ending frontmatter delimiter')
    data: dict[str, str] = {}
    for line in content[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.match(r'^([a-z][a-z0-9_]*):\s*(.*)$', line)
        if not match:
            raise ValueError(f'unsupported or malformed header line: {line!r}')
        key, value = match.groups()
        if key in data:
            raise ValueError(f'duplicate key {key}')
        data[key] = value.strip().strip('"\'')
    return data


def list_ids(value: str) -> list[str]:
    if not (value.startswith('[') and value.endswith(']')):
        return []
    inside = value[1:-1].strip()
    return [i.strip().strip('"\'') for i in inside.split(',') if i.strip()] if inside else []


def validate_file(file: Path, known_ids: set[str] | None = None) -> list[str]:
    errors: list[str] = []
    kind = file.parent.name
    if kind not in SCHEMAS or file.name == 'TEMPLATE.md':
        return errors
    prefix, rtype, required = SCHEMAS[kind]
    try:
        data = frontmatter(file.read_text(encoding='utf-8'))
    except (ValueError, UnicodeError) as e:
        return [f'{file}: {e}']
    for key in required:
        if key not in data:
            errors.append(f'{file}: missing {key}')
    rid = data.get('id', '')
    if not re.fullmatch(rf'{prefix}-\d{{4,}}', rid):
        errors.append(f'{file}: malformed ID {rid!r}')
    if rid and file.stem != rid:
        errors.append(f'{file}: filename must match record id {rid}')
    if data.get('record_type') != rtype:
        errors.append(f'{file}: record_type should be {rtype}')
    if 'created_at' in data:
        try:
            dt = datetime.fromisoformat(data['created_at'])
            if dt.tzinfo is None: raise ValueError('no timezone')
        except ValueError:
            errors.append(f'{file}: created_at must be timezone-aware ISO 8601')
    if kind in VALID_STATUS and data.get('status') not in VALID_STATUS[kind]:
        errors.append(f'{file}: invalid status {data.get("status")!r}')
    if kind == 'evidence' and data.get('verification_status') not in VALID_VERIFICATION:
        errors.append(f'{file}: unsupported verification_status')
    for key in ('goal_id','supersedes'):
        value = data.get(key, '')
        if value and value != 'null' and known_ids is not None and value not in known_ids:
            errors.append(f'{file}: {key} missing referenced record {value}')
    for key in ('hypothesis_ids','related_hypotheses','competing_hypotheses'):
        if key in data and known_ids is not None:
            for hid in list_ids(data[key]):
                if hid not in known_ids:
                    errors.append(f'{file}: {key} missing referenced record {hid}')
    if kind == 'hypotheses' and data.get('status') in {'TESTABLE','QUEUED','TESTING','EVALUATED'}:
        if any(data.get(k,'').strip() in {'','[]'} for k in ('assumptions','predictions','falsifiers')):
            errors.append(f'{file}: TESTABLE+ requires assumptions, predictions and falsifiers')
    if kind == 'experiments' and data.get('status') in {'APPROVED','QUEUED','RUNNING','COMPLETED'}:
        for key in ('protocol','primary_metric','precommitted_success_rule','precommitted_stop_rule','budget'):
            if data.get(key,'').strip() in {'','[]'}:
                errors.append(f'{file}: {data.get("status")} requires nonempty {key}')
    return errors


def validate_all() -> tuple[int, list[str]]:
    paths = [p for kind in SCHEMAS for p in sorted((RESEARCH / kind).glob('*.md')) if p.name != 'TEMPLATE.md']
    known_ids: set[str] = set()
    errors: list[str] = []
    for p in paths:
        try:
            rid = frontmatter(p.read_text(encoding='utf-8')).get('id','')
        except ValueError:
            continue
        if rid in known_ids:
            errors.append(f'{p}: duplicate ID {rid}')
        known_ids.add(rid)
    for p in paths:
        errors.extend(validate_file(p,known_ids))
    return len(paths), errors


if __name__ == '__main__':
    count, errors = validate_all()
    print(f'Research records: {count} checked; {len(errors)} error(s)')
    for err in errors:
        print('ERROR:', err)
    sys.exit(1 if errors else 0)
