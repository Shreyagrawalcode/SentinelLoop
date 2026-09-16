from datetime import datetime, timedelta
import sqlite3

DB_PATH = "sentinelloop.db"

def check_detection(attack_id, time_window_seconds=300):
    """Check if attack was detected within time window"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("SELECT timestamp, technique_id, target FROM attacks WHERE id = ?", (attack_id,))
    attack = c.fetchone()
    
    if not attack:
        return {"status": "NOT_FOUND"}
    
    attack_time = datetime.fromisoformat(attack[0])
    technique_id = attack[1]
    
    # Query Wazuh alerts (placeholder — will connect to Wazuh API later)
    c.execute("SELECT COUNT(*) FROM alerts WHERE technique_id = ? AND timestamp BETWEEN ? AND ?",
              (technique_id, attack_time, attack_time + timedelta(seconds=time_window_seconds)))
    alert_count = c.fetchone()[0]
    
    conn.close()
    
    return {
        "attack_id": attack_id,
        "detected": alert_count > 0,
        "alert_count": alert_count,
        "status": "DETECTED" if alert_count > 0 else "MISSED"
    }
