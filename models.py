class TestCase:
    def __init__(self, tc_id, tc_type, description, expected_result):
        self.tc_id = tc_id
        self.tc_type = tc_type
        self.description = description
        self.expected_result = expected_result

    def to_dict(self):
        return {
            "id": self.tc_id,
            "type": self.tc_type,
            "description": self.description,
            "expected_result": self.expected_result
        }