import sqlite3
import json
from datetime import datetime
import subprocess

DB_PATH = "sentinelloop.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attacks
                 (id INTEGER PRIMARY KEY, technique_id TEXT, timestamp TEXT, target TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def log_attack(technique_id, target, status="PENDING"):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO attacks (technique_id, timestamp, target, status) VALUES (?, ?, ?, ?)",
              (technique_id, timestamp, target, status))
    conn.commit()
    conn.close()
    print(f"[+] Logged: {technique_id} on {target} at {timestamp}")

def run_atomic(technique_id):
    """Trigger Atomic Red Team test"""
    cmd = f"Invoke-AtomicTest {technique_id} -Confirm:$false"
    try:
        subprocess.run(["powershell", "-Command", cmd], check=True)
        log_attack(technique_id, "localhost", "EXECUTED")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    init_db()
    import sys
    if len(sys.argv) > 1:
        run_atomic(sys.argv[1])