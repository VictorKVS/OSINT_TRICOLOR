import tempfile
import unittest
from pathlib import Path
from agent import connect, ingest, normalize_url, report

SAMPLE = {"url": "https://example.org/demo?utm_source=test", "title": "Synthetic example", "category": "trademark", "observed_at": "2026-10-15T09:00:00+03:00", "source": "synthetic"}

class AgentTests(unittest.TestCase):
    def test_normalize_url(self):
        self.assertEqual(normalize_url("https://EXAMPLE.org/demo/?utm_source=test"), "https://example.org/demo")

    def test_dedup(self):
        with tempfile.TemporaryDirectory() as directory:
            db = connect(Path(directory) / "test.db")
            self.assertEqual(ingest(db, SAMPLE)[1], "created")
            self.assertEqual(ingest(db, SAMPLE)[1], "duplicate_seen")
            self.assertEqual(db.execute("SELECT count(*) FROM findings").fetchone()[0], 1)
            db.close()

    def test_report_disclaimer(self):
        with tempfile.TemporaryDirectory() as directory:
            db = connect(Path(directory) / "test.db")
            ingest(db, SAMPLE)
            self.assertIn("Human review required", report(db))
            db.close()

    def test_missing_timezone(self):
        with tempfile.TemporaryDirectory() as directory:
            db = connect(Path(directory) / "test.db")
            with self.assertRaises(ValueError):
                ingest(db, {**SAMPLE, "observed_at": "2026-10-15T09:00:00"})
            db.close()

if __name__ == "__main__":
    unittest.main()
