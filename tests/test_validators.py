"""Dependency-free validator unit tests."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

skills = load('validate_skills')
records = load('validate_records')

class SkillTests(unittest.TestCase):
    def test_all_skills_valid(self):
        count, errors = skills.check_all()
        self.assertEqual(count, 16)
        self.assertEqual(errors, [])

    def test_missing_frontmatter_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            f = Path(t)/'a'/'SKILL.md'
            f.parent.mkdir()
            f.write_text('# Missing header')
            self.assertTrue(skills.validate_skill(f))

class RecordTests(unittest.TestCase):
    def test_template_frontmatter_parsed(self):
        data=records.frontmatter((ROOT/'research'/'hypotheses'/'TEMPLATE.md').read_text())
        self.assertEqual(data['record_type'],'Hypothesis')

    def test_valid_record(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'hypotheses'/'H-0001.md';p.parent.mkdir()
            p.write_text('''---\nid: H-0001\nrecord_type: Hypothesis\ngoal_id: G-0001\nversion: 1\nstatus: TESTABLE\ncreated_at: 2026-11-07T00:00:00+00:00\nclaim: Test hypothesis\nassumptions: [a]\npredictions: [b]\nfalsifiers: [c]\n---\n# Details\n''')
            self.assertEqual(records.validate_file(p,{'G-0001','H-0001'}),[])

    def test_missing_falsifier_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'hypotheses'/'H-0001.md';p.parent.mkdir()
            p.write_text('''---\nid: H-0001\nrecord_type: Hypothesis\ngoal_id: G-0001\nversion: 1\nstatus: TESTABLE\ncreated_at: 2026-11-07T00:00:00+00:00\nclaim: Test\nassumptions: [a]\npredictions: [b]\nfalsifiers: []\n---\n''')
            self.assertTrue(any('falsifiers' in x for x in records.validate_file(p,{'G-0001','H-0001'})))

    def test_invalid_reference_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'hypotheses'/'H-0001.md';p.parent.mkdir()
            p.write_text('''---\nid: H-0001\nrecord_type: Hypothesis\ngoal_id: G-9999\nversion: 1\nstatus: PROPOSED\ncreated_at: 2026-11-07T00:00:00+00:00\nclaim: Test\nassumptions: []\npredictions: []\nfalsifiers: []\n---\n''')
            self.assertTrue(any('G-9999' in x for x in records.validate_file(p,{'H-0001'})))

if __name__ == '__main__': unittest.main()
