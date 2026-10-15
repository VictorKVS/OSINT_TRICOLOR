"""Offline intake MVP for FATHER OSINT TRICOLOR. No network activity."""
import argparse
import datetime as dt
import hashlib
import json
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

DB = Path(__file__).with_name("findings.sqlite3")
WEIGHTS = {"suspected_restream": 65, "suspected_iptv": 50, "trademark": 40, "suspected_counterfeit": 55, "phishing": 90, "other": 20}

def normalize_url(url):
    p = urlsplit(str(url).strip())
    if p.scheme.lower() not in {"http", "https"} or not p.hostname or p.username or p.password:
        raise ValueError("Expected http(s) URL without credentials")
    host = p.hostname.lower()
    port = f":{p.port}" if p.port else ""
    query = urlencode(sorted((k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if k.lower() not in {"fbclid", "yclid"} and not k.lower().startswith("utm_")))
    return urlunsplit((p.scheme.lower(), host + port, p.path.rstrip("/") or "/", query, ""))

def connect(path=DB):
    con = sqlite3.connect(str(path))
    con.execute("PRAGMA foreign_keys=ON")
    con.executescript("""
CREATE TABLE IF NOT EXISTS findings (
 id INTEGER PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, url TEXT NOT NULL,
 category TEXT NOT NULL, title TEXT NOT NULL, description TEXT NOT NULL,
 observed_at TEXT NOT NULL, first_seen TEXT NOT NULL, last_seen TEXT NOT NULL,
 source TEXT NOT NULL, score INTEGER NOT NULL, status TEXT NOT NULL DEFAULT 'needs_review');
CREATE TABLE IF NOT EXISTS audit_log (
 id INTEGER PRIMARY KEY, finding_id INTEGER REFERENCES findings(id),
 action TEXT NOT NULL, logged_at TEXT NOT NULL, details TEXT NOT NULL);
""")
    con.commit()
    return con

def ingest(con, item):
    cat = item["category"]
    if cat not in WEIGHTS:
        raise ValueError("Unsupported category")
    url = normalize_url(item["url"])
    title = str(item["title"]).strip()[:500]
    if not title:
        raise ValueError("Missing title")
    observed = dt.datetime.fromisoformat(item["observed_at"].replace("Z", "+00:00"))
    if observed.utcoffset() is None:
        raise ValueError("Timezone required")
    description = str(item.get("description", ""))[:5000]
    source = str(item.get("source", "manual"))[:200]
    fingerprint = hashlib.sha256(f"{cat}|{url}".encode()).hexdigest()
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    existing = con.execute("SELECT id FROM findings WHERE fingerprint=?", (fingerprint,)).fetchone()
    if existing:
        case_id = existing[0]
        action = "duplicate_seen"
        con.execute("UPDATE findings SET last_seen=? WHERE id=?", (now, case_id))
    else:
        cur = con.execute("""INSERT INTO findings
(fingerprint,url,category,title,description,observed_at,first_seen,last_seen,source,score)
VALUES (?,?,?,?,?,?,?,?,?,?)""", (fingerprint, url, cat, title, description, observed.isoformat(), now, now, source, WEIGHTS[cat]))
        case_id = cur.lastrowid
        action = "created"
    con.execute("INSERT INTO audit_log(finding_id,action,logged_at,details) VALUES(?,?,?,?)",
        (case_id, action, now, json.dumps({"source": source, "url": url}, ensure_ascii=False)))
    con.commit()
    return case_id, action

def report(con):
    rows = con.execute("SELECT id,category,score,title,url,status FROM findings ORDER BY score DESC,id").fetchall()
    lines = ["# Preliminary OSINT signals", "", "**Not verified infringements or accusations. Human review required.**", "", f"Unique signals: {len(rows)}", ""]
    for case_id, cat, score, title, url, status in rows:
        lines.extend([f"## CASE-{case_id:05d} · {cat} · priority {score}/100", f"- Title: {title}", f"- URL: {url}", f"- Review: {status}", "- Next: verify rights, context, and licensing with a qualified specialist.", ""])
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Offline OSINT TRIAGE demo; no network collection")
    parser.add_argument("command", choices=["init", "import", "report"])
    parser.add_argument("path", nargs="?")
    args = parser.parse_args()
    with connect() as con:
        if args.command == "init":
            print(f"Initialized: {DB}")
        elif args.command == "report":
            output = Path(__file__).with_name("report_generated.md")
            output.write_text(report(con), encoding="utf-8")
            print(f"Saved: {output}")
        else:
            if not args.path:
                parser.error("import requires path to JSONL")
            for lineno, line in enumerate(Path(args.path).read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    case_id, action = ingest(con, json.loads(line))
                    print(f"line {lineno}: CASE-{case_id:05d} {action}")
                except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
                    print(f"line {lineno}: rejected: {exc}")
if __name__ == "__main__":
    main()
