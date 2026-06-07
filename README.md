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


## Current Status

This project is under development for the Microsoft Agents League Hackathon.
