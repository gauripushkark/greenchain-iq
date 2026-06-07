from pathlib import Path

from risk_scoring import load_suppliers, evaluate_supplier, print_supplier_report
from prompts import SYSTEM_PROMPT, DEMO_QUESTION
from knowledge_base import get_grounding_for_supplier

def print_project_intro():
    """Print a simple project introduction for the demo."""
    print("=" * 80)
    print("GreenChain IQ: Supplier Sustainability Risk Agent")
    print("=" * 80)
    print()
    print("Project Purpose:")
    print(
        "GreenChain IQ helps evaluate supplier sustainability risk using "
        "synthetic ESG data and grounded policy guidance."
    )
    print()
    print("Hackathon Track:")
    print("Reasoning Agents")
    print()
    print("Microsoft IQ Layer:")
    print("Foundry IQ")
    print()
    print("Demo Question:")
    print(DEMO_QUESTION.strip())
    print()


def summarize_portfolio(results):
    """Print a portfolio-level summary of supplier risk results."""
    risk_counts = {"High": 0, "Medium": 0, "Low": 0}

    for result in results:
        risk_counts[result["risk_level"]] += 1

    print("=" * 80)
    print("Portfolio-Level Risk Summary")
    print("=" * 80)
    print(f"High Risk Suppliers: {risk_counts['High']}")
    print(f"Medium Risk Suppliers: {risk_counts['Medium']}")
    print(f"Low Risk Suppliers: {risk_counts['Low']}")
    print()

    high_risk_suppliers = [
        result["supplier"] for result in results if result["risk_level"] == "High"
    ]

    if high_risk_suppliers:
        print("High Risk Supplier List:")
        for supplier in high_risk_suppliers:
            print(f"- {supplier}")
    else:
        print("No high-risk suppliers were identified in the synthetic dataset.")

    print()


def print_responsible_ai_note():
    """Print responsible AI and data safety note."""
    print("=" * 80)
    print("Responsible AI and Data Safety Note")
    print("=" * 80)
    print(
        "This demo uses only synthetic supplier data. It does not include "
        "confidential employer, client, vendor, or personal information."
    )
    print(
        "The agent is designed as a decision-support tool and does not replace "
        "human compliance, legal, procurement, or sustainability review."
    )
    print()


def main():
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "suppliers_sample.csv"

    print_project_intro()

    print("System Prompt Preview:")
    print(SYSTEM_PROMPT.strip()[:700])
    print("...")
    print()

    suppliers = load_suppliers(csv_path)
    results = [evaluate_supplier(supplier) for supplier in suppliers]

    summarize_portfolio(results)

    print("=" * 80)
    print("Detailed Supplier Risk Reports")
    print("=" * 80)
    print()

    for result in results:
    print_supplier_report(result)

    grounding_items = get_grounding_for_supplier(result["reasoning"])

    print("Grounded Policy Guidance:")
    for item in grounding_items:
        print(f"- Source: {item['source']}")
        print(f"  Guidance: {item['excerpt']}")
    print()

    print_responsible_ai_note()


if __name__ == "__main__":
    main()
