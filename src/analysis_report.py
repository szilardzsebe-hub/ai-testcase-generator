from config import ANALYSIS_REPORT_FILE


def create_analysis_report(requirement, analysis, index):

    with open(ANALYSIS_REPORT_FILE, "a", encoding="utf-8") as file:

        file.write(f"Requirement #{index}\n")
        file.write("-" * 30 + "\n")

        file.write(f"{requirement}\n\n")

        file.write("Category\n")
        file.write("-" * 10 + "\n")
        file.write(f"{analysis.category}\n\n")

        file.write("Keywords\n")
        file.write("-" * 10 + "\n")

        for keyword in analysis.keywords:
            file.write(f"• {keyword}\n")

        file.write("\nRisks\n")
        file.write("-" * 10 + "\n")

        for risk in analysis.risks:
            file.write(f"• {risk}\n")

        file.write("\nValidations\n")
        file.write("-" * 12 + "\n")

        for validation in analysis.validations:
            file.write(f"• {validation}\n")

        file.write("\n")
        file.write("=" * 50 + "\n\n")




def initialize_analysis_report():

    ANALYSIS_REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(ANALYSIS_REPORT_FILE, "w", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write("AI Assisted Test Case Generator\n")
        file.write("Requirement Analysis Report\n")
        file.write("=" * 50 + "\n\n")