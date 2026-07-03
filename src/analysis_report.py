from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "output" / "analysis_report.md"


def create_analysis_report(requirement, analysis):

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "a", encoding="utf-8") as file:

        file.write("# Requirement Analysis\n\n")

        file.write("## Requirement\n\n")
        file.write(f"{requirement}\n\n")

        file.write("## Category\n\n")
        file.write(f"{analysis.category}\n\n")

        file.write("## Keywords\n\n")
        for keyword in analysis.keywords:
            file.write(f"- {keyword}\n")

        file.write("\n## Risks\n\n")
        for risk in analysis.risks:
            file.write(f"- {risk}\n")

        file.write("\n## Validations\n\n")
        for validation in analysis.validations:
            file.write(f"- {validation}\n")

        file.write("\n---\n\n")