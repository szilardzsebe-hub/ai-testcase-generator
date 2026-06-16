import sqlite3

from pathlib import Path
from models import TestCase

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "tc.db"




def init_db():
   
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tc_counter (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        value INTEGER NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS generated_testcases (
        requirement TEXT,
        tc_id TEXT,
        tc_type TEXT,
        description TEXT,
        expected_result TEXT
    )
    """)
    
 

    cur.execute(
        "INSERT OR IGNORE INTO tc_counter (id, value) VALUES (1, 0)"
    )

    conn.commit()
    conn.close()


def next_tc_id():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT value FROM tc_counter WHERE id = 1")
    current = cur.fetchone()[0]

    next_value = current + 1

    cur.execute(
        "UPDATE tc_counter SET value = ? WHERE id = 1",
        (next_value,)
    )

    conn.commit()
    conn.close()

    return f"TC-{next_value:03d}"


def get_existing_test_cases(requirement):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    normalized = requirement.strip().lower()

    cur.execute("""
        SELECT tc_id, tc_type, description, expected_result
        FROM generated_testcases
        WHERE requirement = ?
        ORDER BY tc_id
    """, (normalized,))

    rows = cur.fetchall()

    conn.close()

    return [
        TestCase(
            tc_id,
            tc_type,
            description,
            expected_result
        )
        for tc_id, tc_type, description, expected_result in rows
    ]

def save_test_cases(requirement, test_cases):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    normalized = requirement.strip().lower()

    for tc in test_cases:
        cur.execute("""
            INSERT INTO generated_testcases (
                requirement,
                tc_id,
                tc_type,
                description,
                expected_result
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            normalized,
            tc.tc_id,
            tc.tc_type,
            tc.description,
            tc.expected_result
        ))

    conn.commit()
    conn.close()

def get_or_generate_test_cases(requirement):

    existing = get_existing_test_cases(requirement)

    if existing:
        print(f"Using cached test cases for: {requirement}")
        return existing

    from generator import generate_test_cases

    generated = generate_test_cases(requirement)

    generated = assign_ids(generated)

    save_test_cases(requirement, generated)

    return generated
def reserve_tc_ids(n):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT value FROM tc_counter WHERE id = 1")
    current = cur.fetchone()[0]

    start = current + 1
    end = current + n

    cur.execute("UPDATE tc_counter SET value = ? WHERE id = 1", (end,))

    conn.commit()
    conn.close()

    return [f"TC-{i:03d}" for i in range(start, end + 1)]
def assign_ids(test_cases):
    ids = reserve_tc_ids(len(test_cases))

    return [
        TestCase(
            ids[i],
            tc.tc_type,
            tc.description,
            tc.expected_result
        )
        for i, tc in enumerate(test_cases)
    ]
