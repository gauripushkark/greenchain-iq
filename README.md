# GreenChain IQ: Supplier Sustainability Risk Agent

GreenChain IQ is a Microsoft Foundry-based reasoning agent that helps analyze supplier sustainability risk using synthetic ESG data and grounded policy guidance from Foundry IQ.

## Project Overview

Sustainability, sourcing, and business analytics teams often need to review supplier ESG data across emissions, labor, waste, water, certifications, and audit recency. This process can be manual, inconsistent, and difficult to explain.

GreenChain IQ demonstrates how an AI reasoning agent can support this workflow by reviewing supplier records, identifying risk drivers, retrieving relevant policy guidance, classifying supplier risk, and recommending prioritized follow-up actions.

## Challenge Track

**Track:** Reasoning Agents
**Microsoft IQ Layer:** Foundry IQ
**Theme:** Sustainability Analytics, ESG Risk, Enterprise AI, Responsible AI

## What the Agent Does

The agent follows a multi-step reasoning workflow:

1. Reviews synthetic supplier ESG data.
2. Checks for missing or outdated information.
3. Retrieves relevant guidance from a Foundry IQ knowledge base.
4. Evaluates sustainability risk across emissions, labor, waste, water, certification status, and audit recency.
5. Classifies each supplier as low, medium, or high risk.
6. Explains the reasoning behind the classification.
7. Recommends prioritized supplier follow-up actions.
8. Produces an executive summary for business stakeholders.

## Microsoft IQ Integration

This project uses Foundry IQ as the required Microsoft IQ intelligence layer. Foundry IQ will be used as a grounded knowledge base containing synthetic policy documents such as:

* Supplier ESG policy
* Risk scoring guide
* Certification requirements
* Audit frequency rules
* Corrective action playbook

The agent uses this knowledge base to ground its explanations and recommendations.

## Architecture

The project architecture is documented in [`docs/architecture.md`](docs/architecture.md).

The MVP currently uses a local knowledge retrieval scaffold to demonstrate the intended Foundry IQ retrieval pattern. The final architecture is designed to connect the synthetic policy documents to Foundry IQ as a grounded knowledge base for the Microsoft Foundry reasoning agent.


## Responsible AI and Data Safety

This project uses only synthetic demo data. It does not include confidential employer, client, vendor, or personal information.

The agent is designed as a decision-support tool. It does not replace human compliance, legal, procurement, or sustainability review.

## Repository Structure

greenchain-iq/
│
├── README.md
├── data/
│   └── suppliers_sample.csv
├── docs/
│   ├── supplier_esg_policy.md
│   ├── risk_scoring_guide.md
│   ├── certification_requirements.md
│   ├── audit_frequency_rules.md
│   └── corrective_action_playbook.md
├── src/
│   ├── risk_scoring.py
│   ├── prompts.py
│   └── app.py
└── assets/
    └── architecture.png


## How to Run the MVP Demo

This project currently includes a command-line MVP demo that reads synthetic supplier ESG data and classifies each supplier as Low, Medium, or High Risk.

### Run in GitHub Codespaces or a local Python environment

```bash
python src/app.py
```

If your environment uses Python 3 explicitly, run:

```bash
python3 src/app.py
```

### Expected Output

The demo prints:

* Project overview
* Hackathon track and Microsoft IQ layer
* Agent prompt preview
* Portfolio-level supplier risk summary
* Detailed supplier-level risk reports
* Responsible AI and data safety note

Example portfolio summary:

```text
High Risk Suppliers: 4
Medium Risk Suppliers: 1
Low Risk Suppliers: 3
```

## MVP Capabilities

The current MVP can:

1. Read synthetic supplier ESG data from a CSV file.
2. Evaluate emissions, labor, waste, and water scores.
3. Check certification status.
4. Check audit recency using a fixed hackathon demo reference date.
5. Classify suppliers as Low, Medium, or High Risk.
6. Explain the risk drivers.
7. Recommend follow-up actions.
8. Print an executive summary for each supplier.

## Grounded Knowledge Retrieval Scaffold

The MVP includes a local knowledge retrieval scaffold that reads synthetic policy documents from the `docs/` folder and selects relevant guidance based on the supplier's risk drivers.

This scaffold demonstrates the intended retrieval pattern for the final Foundry IQ integration:

```text
Supplier ESG data
  → Risk scoring logic
  → Risk drivers
  → Relevant policy document selection
  → Grounded policy guidance
  → Business-ready recommendations
```

The current local retrieval layer uses synthetic markdown documents such as:

* `supplier_esg_policy.md`
* `risk_scoring_guide.md`
* `certification_requirements.md`
* `audit_frequency_rules.md`
* `corrective_action_playbook.md`

In the next phase, these documents are intended to be connected to Foundry IQ as a grounded knowledge base for the reasoning agent.


## Next Planned Enhancements

The next phase is to connect the synthetic policy documents in the `docs/` folder to Foundry IQ and use them as a grounded knowledge base for the reasoning agent.


## Current Status

This project is under development for the Microsoft Agents League Hackathon.
