"""Validate *metadata completeness* of synthetic sample evidence records.

Never interprets validity, efficacy, dosing, or clinical risk of a supplement.
"""
import argparse
import csv
import json
from pathlib import Path

REQUIRED = ('claim_id', 'supplement', 'claim', 'source_title', 'source_url', 'evidence_grade')
GRADES = {'preliminary', 'moderate', 'strong'}


def audit(file_path):
    """Return (records_count, problems) for a CSV file."""
    issues = []
    seen = set()
    with Path(file_path).open(newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        missing = [field for field in REQUIRED if field not in (reader.fieldnames or [])]
        if missing:
            return 0, [{'row': 1, 'issue': 'missing columns: ' + ', '.join(missing)}]
        count = 0
        for row in reader:
            count += 1
            row_no = count + 1
            for field in REQUIRED:
                if not (row.get(field) or '').strip():
                    issues.append({'row': row_no, 'issue': 'missing ' + field})
            identifier = (row.get('claim_id') or '').strip()
            if identifier and identifier in seen:
                issues.append({'row': row_no, 'issue': 'duplicate claim_id ' + identifier})
            seen.add(identifier)
            url = (row.get('source_url') or '').strip()
            if url and not url.startswith('https://'):
                issues.append({'row': row_no, 'issue': 'source_url must start with https://'})
            grade = (row.get('evidence_grade') or '').strip().lower()
            if grade and grade not in GRADES:
                issues.append({'row': row_no, 'issue': 'unrecognized evidence_grade ' + grade})
    return count, issues


def main():
    parser = argparse.ArgumentParser(description='Audit CSV metadata (not clinical accuracy).')
    parser.add_argument('csv_file', help='Input CSV with evidence-record metadata')
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    args = parser.parse_args()
    count, issues = audit(args.csv_file)
    if args.format == 'json':
        print(json.dumps({'records': count, 'issues': issues}, indent=2))
    else:
        print(f'Evidence metadata audit: {count} rows; {len(issues)} issues')
        for problem in issues:
            print(f"  row {problem['row']}: {problem['issue']}")
    return 1 if issues else 0


if __name__ == '__main__':
    raise SystemExit(main())
