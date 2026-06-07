from datetime import datetime, date
from pathlib import Path
import csv


# Fixed reference date for hackathon demo consistency.
# The hackathon submission deadline is June 14, 2026, so this keeps audit-age logic stable.
REFERENCE_DATE = date(2026, 6, 14)


ESG_SCORE_COLUMNS = [
    "EmissionsScore",
    "LaborScore",
    "WasteScore",
    "WaterScore",
]


def parse_date(date_text):
    """Convert YYYY-MM-DD text into a date object."""
    if not date_text:
        return None

    try:
        return datetime.strptime(date_text, "%Y-%m-%d").date()
    except ValueError:
        return None


def months_between(start_date, end_date):
    """Approximate full months between two dates."""
    if start_date is None:
        return None

    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


def get_score_issues(row):
    """Identify ESG score issues for a supplier."""
    issues = []
    low_score_count = 0
    high_risk_score_found = False

    for column in ESG_SCORE_COLUMNS:
        try:
            score = int(row[column])
        except (ValueError, KeyError):
            issues.append(f"{column} is missing or invalid.")
            high_risk_score_found = True
            continue

        readable_name = column.replace("Score", " score")

        if score < 50:
            issues.append(f"{readable_name} is {score}, which is below the high-risk threshold of 50.")
            high_risk_score_found = True

        if score < 65:
            low_score_count += 1

    return issues, low_score_count, high_risk_score_found


def evaluate_supplier(row):
    """
    Evaluate one supplier record and return risk classification,
    reasoning, and recommended actions.
    """
    supplier_name = row.get("Supplier", "Unknown supplier")
    certification_status = row.get("CertificationStatus", "").strip()
    last_audit_date = parse_date(row.get("LastAuditDate", ""))
    audit_age_months = months_between(last_audit_date, REFERENCE_DATE)
    notes = row.get("Notes", "").strip()

    reasoning = []
    recommended_actions = []

    score_issues, low_score_count, high_risk_score_found = get_score_issues(row)
    reasoning.extend(score_issues)

    missing_certification = certification_status.lower() == "missing"
    pending_certification = certification_status.lower() == "pending"
    outdated_audit = audit_age_months is not None and audit_age_months > 12
    missing_audit_date = last_audit_date is None

    if missing_certification:
        reasoning.append("Certification status is missing, which requires supplier documentation follow-up.")
        recommended_actions.append("Request updated sustainability or environmental certification.")

    if pending_certification:
        reasoning.append("Certification status is pending and should be tracked until resolved.")
        recommended_actions.append("Follow up on pending certification status.")

    if missing_audit_date:
        reasoning.append("Last audit date is missing or invalid.")
        recommended_actions.append("Request updated supplier audit information.")

    if outdated_audit:
        reasoning.append(
            f"Last audit date is {row.get('LastAuditDate')}, which is older than the 12-month refresh window."
        )
        recommended_actions.append("Schedule an updated supplier sustainability audit.")

    if low_score_count >= 2:
        reasoning.append(f"{low_score_count} ESG scores are below 65, indicating multiple sustainability gaps.")

    if "water" in notes.lower():
        recommended_actions.append("Request a water usage reduction plan.")

    if "waste" in notes.lower():
        recommended_actions.append("Request a waste reduction or recycling improvement plan.")

    if "labor" in notes.lower():
        recommended_actions.append("Request labor practice documentation and corrective action details.")

    if high_risk_score_found:
        recommended_actions.append("Add supplier to high-priority sustainability review.")

    if low_score_count >= 2:
        recommended_actions.append("Add supplier to quarterly monitoring.")

    # Risk classification logic
    if (
        high_risk_score_found
        or missing_certification
        or outdated_audit
        or missing_audit_date
        or low_score_count >= 2
    ):
        risk_level = "High"
    elif pending_certification or low_score_count == 1:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    if not reasoning:
        reasoning.append("Supplier meets the low-risk criteria based on available synthetic ESG data.")

    if not recommended_actions:
        recommended_actions.append("Continue standard annual supplier sustainability monitoring.")

    executive_summary = (
        f"{supplier_name} is classified as {risk_level} Risk based on the synthetic ESG review. "
        f"The main drivers are: {' '.join(reasoning[:2])}"
    )

    return {
        "supplier": supplier_name,
        "risk_level": risk_level,
        "reasoning": reasoning,
        "recommended_actions": list(dict.fromkeys(recommended_actions)),
        "executive_summary": executive_summary,
    }


def load_suppliers(csv_path):
    """Load supplier records from CSV."""
    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def print_supplier_report(result):
    """Print a readable supplier risk report."""
    print("=" * 80)
    print(f"Supplier: {result['supplier']}")
    print(f"Risk Level: {result['risk_level']}")
    print("\nReasoning:")

    for index, item in enumerate(result["reasoning"], start=1):
        print(f"{index}. {item}")

    print("\nRecommended Actions:")

    for action in result["recommended_actions"]:
        print(f"- {action}")

    print("\nExecutive Summary:")
    print(result["executive_summary"])
    print("=" * 80)
    print()


def main():
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "suppliers_sample.csv"

    suppliers = load_suppliers(csv_path)

    print("GreenChain IQ: Supplier Sustainability Risk Report")
    print(f"Reference Date: {REFERENCE_DATE}")
    print(f"Suppliers Reviewed: {len(suppliers)}")
    print()

    for supplier in suppliers:
        result = evaluate_supplier(supplier)
        print_supplier_report(result)


if __name__ == "__main__":
    main()
