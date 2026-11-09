#!/usr/bin/env python3
"""Offline structural validation of Codex skills (no LLM calls)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'
REQUIRED = ('## Purpose', '## Inputs', '## Procedure', '## Required artifacts', '## Acceptance checks', '## Default handoff')


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    txt = path.read_text(encoding='utf-8')
    if not txt.startswith('---\n'):
        return [f'{path}: missing YAML front matter']
    parts = txt.split('---\n', 2)
    if len(parts) < 3:
        return [f'{path}: unterminated YAML front matter']
    header, body = parts[1], parts[2]
    name = re.search(r'^name:\s*(\S+)\s*$', header, re.MULTILINE)
    desc = re.search(r'^description:\s*(.+?)\s*$', header, re.MULTILINE)
    if not name or name.group(1) != path.parent.name:
        errors.append(f'{path}: front matter name does not match folder')
    if not desc or len(desc.group(1).strip()) < 40:
        errors.append(f'{path}: missing/inadequate description')
    for heading in REQUIRED:
        if heading not in body and path.parent.name != 'hypothesis-discovery':
            errors.append(f'{path}: missing section {heading}')
    if 'LLM API' not in body and 'model API' not in body:
        errors.append(f'{path}: missing no-model-API boundary')
    if len(body) < 1000:
        errors.append(f'{path}: suspiciously short skill instructions')
    return errors


def check_all() -> tuple[int, list[str]]:
    paths = sorted(SKILLS.glob('*/SKILL.md'))
    errors = []
    seen = set()
    for path in paths:
        if path.parent.name in seen:
            errors.append(f'duplicate name {path.parent.name}')
        seen.add(path.parent.name)
        errors.extend(validate_skill(path))
    if not paths:
        errors.append('no skills found')
    if not (SKILLS / 'README.md').is_file():
        errors.append('missing skill catalogue')
    index_text = (SKILLS / 'README.md').read_text(encoding='utf-8')
    for p in paths:
        if f'({p.parent.name}/SKILL.md)' not in index_text:
            errors.append(f'{p}: not listed in skill catalogue')
        content = p.read_text(encoding='utf-8')
        for target in re.findall(r'Continue with `([a-z][a-z-]+)`', content):
            if not (SKILLS / target / 'SKILL.md').is_file():
                errors.append(f'{p}: missing handoff skill {target}')
    for link in re.findall(r'\]\(([^)]+\.md)\)', index_text):
        if not (SKILLS / link).resolve().is_file():
            errors.append(f'skill catalogue: broken link {link}')
    return len(paths), errors


if __name__ == '__main__':
    count, errors = check_all()
    print(f'Skill catalogue: {count} skills; {len(errors)} error(s)')
    for e in errors:
        print('ERROR:', e)
    sys.exit(1 if errors else 0)
