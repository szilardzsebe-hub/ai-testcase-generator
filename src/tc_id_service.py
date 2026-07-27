import sqlite3
from models import TestCase
from config import DATABASE_FILE
import json

from models import (
    TestCase,
    TestType,
    Priority,
    AutomationCandidate,
)





def init_db():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS tc_counter (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            value INTEGER NOT NULL
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS generated_testcases (
                tc_id TEXT PRIMARY KEY,
                title TEXT,
                requirement TEXT,
                category TEXT,
                tc_type TEXT,
                priority TEXT,
                preconditions TEXT,
                test_data TEXT,
                steps TEXT,
                expected_result TEXT,
                postconditions TEXT,
                automation_candidate TEXT,
                tags TEXT
            )
        """)

        cur.execute("""
            INSERT OR IGNORE INTO tc_counter (id, value)
            VALUES (1, 0)
        """)

        conn.commit()

def get_existing_test_cases(requirement):

    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        normalized = requirement.strip().lower()

        cur.execute("""
            SELECT
                tc_id,
                title,
                requirement,
                category,
                tc_type,
                priority,
                preconditions,
                test_data,
                steps,
                expected_result,
                postconditions,
                automation_candidate,
                tags
            FROM generated_testcases
            WHERE requirement = ?
            ORDER BY tc_id
        """, (normalized,))

        rows = cur.fetchall()

    return [
    TestCase(
        tc_id=tc_id,
        title=title,
        requirement=requirement,
        category=category,
        tc_type=TestType(tc_type),
        priority=Priority(priority),
        preconditions=json.loads(preconditions),
        test_data=json.loads(test_data),
        steps=json.loads(steps),
        expected_result=expected_result,
        postconditions=json.loads(postconditions),
        automation_candidate=AutomationCandidate(automation_candidate),
        tags=json.loads(tags),
    )
    for (
        tc_id,
        title,
        requirement,
        category,
        tc_type,
        priority,
        preconditions,
        test_data,
        steps,
        expected_result,
        postconditions,
        automation_candidate,
        tags,
    ) in rows

         
    ]

def save_test_cases(requirement, test_cases):
    print("=== NEW SAVE FUNCTION ===")

    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        normalized = requirement.strip().lower()

        for tc in test_cases:
            print("tc_id:", tc.tc_id, type(tc.tc_id))
            print("title:", tc.title, type(tc.title))
            print("requirement:", tc.requirement, type(tc.requirement))
            print("category:", tc.category, type(tc.category), tc.category.value)
            print("tc_type:", tc.tc_type, type(tc.tc_type), tc.tc_type.value)
            print("priority:", tc.priority, type(tc.priority), tc.priority.value)
            print("preconditions:", type(tc.preconditions))
            print("test_data:", type(tc.test_data))
            print("steps:", type(tc.steps))
            print("expected_result:", tc.expected_result, type(tc.expected_result))
            print("postconditions:", type(tc.postconditions))
            print("automation:", tc.automation_candidate, type(tc.automation_candidate), tc.automation_candidate.value)
            print("tags:", type(tc.tags))
            cur.execute(
                """
                INSERT INTO generated_testcases (
                    tc_id,
                    title,
                    requirement,
                    category,
                    tc_type,
                    priority,
                    preconditions,
                    test_data,
                    steps,
                    expected_result,
                    postconditions,
                    automation_candidate,
                    tags
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    tc.tc_id,
                    tc.title,
                    tc.requirement,
                    tc.category.value,
                    tc.tc_type.value,
                    tc.priority.value,
                    json.dumps(tc.preconditions),
                    json.dumps(tc.test_data),
                    json.dumps(tc.steps),
                    tc.expected_result,
                    json.dumps(tc.postconditions),
                    tc.automation_candidate.value,
                    json.dumps(tc.tags),
                ),
            )

        conn.commit()

 

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

    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        cur.execute("SELECT value FROM tc_counter WHERE id = 1")
        current = cur.fetchone()[0]

        start = current + 1
        end = current + n

        cur.execute(
            "UPDATE tc_counter SET value = ? WHERE id = 1",
            (end,)
        )

        conn.commit()

    return [
        f"TC-{i:03d}"
        for i in range(start, end + 1)
    ]

  
def assign_ids(test_cases):
    """
    Assigns unique Test Case IDs to newly generated test cases.

    The function updates the existing TestCase objects instead of creating
    new ones. This preserves all metadata (priority, preconditions,
    test data, steps, tags, etc.) introduced in V1.4.
    """

    ids = reserve_tc_ids(len(test_cases))

    for i, tc in enumerate(test_cases):
        tc.tc_id = ids[i]

    return test_cases
