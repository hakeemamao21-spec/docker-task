import copy
from typing import List, Tuple, Dict, Any

def is_valid_id(student_id: str) -> bool:
    if not isinstance(student_id, str):
        return False
    if len(student_id) != 4:
        return False
    if not student_id.startswith('S'):
        return False

    tail = student_id[1:]
    return tail.isdigit()


def clean_data(raw_records: List[Tuple[str, str, str, float]]) -> Tuple[List[Tuple[str, str, str, float]], int]:
    valid_records = []
    invalid_count = 0

    for rec in raw_records:
        if not (isinstance(rec, tuple) and len(rec) == 4):
            invalid_count += 1
            continue

        student_id, course_code, prereq_status, current_score = rec

        if not is_valid_id(student_id):
            invalid_count += 1
            continue

        if prereq_status != "MET_PREREQ":
            invalid_count += 1
            continue

        valid_records.append(rec)

    return (valid_records, invalid_count)


sample_data = [
    ("S123", "CS100", "MET_PREREQ", 85.0),
    ("S12X", "CS100", "MET_PREREQ", 90.0),   # invalid ID
    ("S999", "CS101", "NO_PREREQ", 88.0),    # prereq not met
    ("BAD",  "CS102", "MET_PREREQ", 77.0)    # invalid format
]

result = clean_data(sample_data)
print(result)