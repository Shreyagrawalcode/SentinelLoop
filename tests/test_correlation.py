import sys
sys.path.insert(0, '../backend')
from correlation import check_detection
import sqlite3

def test_detection_missed():
    """Test when attack has no matching alert"""
    result = check_detection(1)
    assert result['status'] in ['NOT_FOUND', 'MISSED']

def test_detection_found():
    """Test when attack has matching alert"""
    # Insert mock data first
    conn = sqlite3.connect('sentinelloop.db')
    c = conn.cursor()
    c.execute("INSERT INTO attacks (technique_id, timestamp, target, status) VALUES (?, ?, ?, ?)",
              ('T1059.001', '2024-01-01T10:00:00', 'localhost', 'EXECUTED'))
    c.execute("INSERT INTO alerts (technique_id, timestamp, rule) VALUES (?, ?, ?)",
              ('T1059.001', '2024-01-01T10:01:00', 'powershell_detected'))
    conn.commit()
    conn.close()
    
    result = check_detection(1)
    assert result['detected'] == True

if __name__ == "__main__":
    test_detection_missed()
    test_detection_found()
    print("✅ All tests passed")