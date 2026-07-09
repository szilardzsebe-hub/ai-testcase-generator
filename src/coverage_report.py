from collections import Counter

from config import COVERAGE_REPORT_FILE

def create_coverage_report(requirements, analyses, test_cases):

    COVERAGE_REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    type_counter = Counter(tc.tc_type for tc in test_cases)

    categories = sorted(set(a.category for a in analyses))

    coverage = (
        len(categories) / len(requirements) * 100
        if requirements else 0
    )

    with open(COVERAGE_REPORT_FILE, "w", encoding="utf-8") as file:

       file.write("=" * 50 + "\n")
       file.write("AI Assisted Test Case Generator\n")
       file.write("Coverage Report\n")
       file.write("=" * 50 + "\n\n")

       file.write(f"Requirements analyzed : {len(requirements)}\n")
       file.write(f"Requirements covered  : {len(categories)}\n")
       file.write(f"Coverage              : {coverage:.0f}%\n\n")

       file.write(f"Generated Test Cases  : {len(test_cases)}\n\n")

       file.write("Test Types\n")
       file.write("-" * 20 + "\n")

       for tc_type, count in sorted(type_counter.items()):
        file.write(f"{tc_type:<10}: {count}\n")

        file.write("\nRequirement Categories\n")
        file.write("-" * 30 + "\n")

       for category in categories:
           file.write(f"✓ {category}\n")