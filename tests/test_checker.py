import tempfile
import unittest
from pathlib import Path
from evidence_checker import audit


class AuditTests(unittest.TestCase):
    def check_csv(self, rows):
        with tempfile.TemporaryDirectory() as dirname:
            file = Path(dirname) / 'claims.csv'
            file.write_text(rows, encoding='utf-8')
            return audit(file)

    def test_clean_record(self):
        count, issues = self.check_csv(
            'claim_id,supplement,claim,source_title,source_url,evidence_grade\n'
            'C001,Example A,Demo text,Fake Article,https://example.com/a,moderate\n'
        )
        self.assertEqual((count, issues), (1, []))

    def test_missing_citation(self):
        count, issues = self.check_csv(
            'claim_id,supplement,claim,source_title,source_url,evidence_grade\n'
            'C001,Example A,Demo text,,https://example.com/a,preliminary\n'
        )
        self.assertEqual(count, 1)
        self.assertIn('missing source_title', [x['issue'] for x in issues])

    def test_duplicate_ids(self):
        count, issues = self.check_csv(
            'claim_id,supplement,claim,source_title,source_url,evidence_grade\n'
            'C001,A,X,Source,https://example.com/a,strong\n'
            'C001,B,Y,Source,https://example.com/b,strong\n'
        )
        self.assertEqual(count, 2)
        self.assertTrue(any('duplicate' in x['issue'] for x in issues))

    def test_missing_column(self):
        count, issues = self.check_csv('claim_id,claim\nC001,X\n')
        self.assertEqual(count, 0)
        self.assertTrue(any('missing columns' in x['issue'] for x in issues))


if __name__ == '__main__':
    unittest.main()
