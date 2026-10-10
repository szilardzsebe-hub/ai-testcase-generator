import json
import sqlite3

from src.config import DATABASE_FILE

from database.sql_queries import (
    CREATE_COUNTER_TABLE,
    CREATE_TESTCASES_TABLE,
    INITIALIZE_COUNTER,
    SELECT_COUNTER,
    UPDATE_COUNTER,
    SELECT_TESTCASES_BY_REQUIREMENT,
    INSERT_TESTCASE,
)
from src.models import (
    TestCase,
    TestType,
    Priority,
    AutomationCandidate,
)

def init_db():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        cur.execute(CREATE_COUNTER_TABLE)

        cur.execute(CREATE_TESTCASES_TABLE)

        cur.execute(INITIALIZE_COUNTER)

        conn.commit()

def get_existing_test_cases(requirement):

    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        normalized = requirement.strip().lower()

        cur.execute(
            SELECT_TESTCASES_BY_REQUIREMENT,
            (normalized,),
)

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

    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        for tc in test_cases:
           
            cur.execute(
                INSERT_TESTCASE,
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

    from src.generator import generate_test_cases

    generated = generate_test_cases(requirement)

    generated = assign_ids(generated)

    save_test_cases(requirement, generated)

    return generated


def reserve_tc_ids(n):

    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        cur.execute(SELECT_COUNTER)
        current = cur.fetchone()[0]

        start = current + 1
        end = current + n

        cur.execute(
            UPDATE_COUNTER,
        (end,),
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
