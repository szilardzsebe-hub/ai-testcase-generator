
"""
Centralized SQL statements used by the persistence layer.

Keeping SQL definitions in a dedicated module improves readability,
maintainability and reuse across the application.
"""

CREATE_COUNTER_TABLE = """
CREATE TABLE IF NOT EXISTS tc_counter (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    value INTEGER NOT NULL
)
"""

CREATE_TESTCASES_TABLE = """
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
"""

INITIALIZE_COUNTER = """
INSERT OR IGNORE INTO tc_counter (id, value)
VALUES (1, 0)
"""

SELECT_COUNTER = """
SELECT value
FROM tc_counter
WHERE id = 1
"""

UPDATE_COUNTER = """
UPDATE tc_counter
SET value = ?
WHERE id = 1
"""

SELECT_TESTCASES_BY_REQUIREMENT = """
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
"""

INSERT_TESTCASE = """
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
"""