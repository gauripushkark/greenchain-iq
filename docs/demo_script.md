# GreenChain IQ Demo Script

## Demo Title

GreenChain IQ: Supplier Sustainability Risk Reasoning Agent

## 1. Introduction

GreenChain IQ is a supplier sustainability risk reasoning agent built for the Microsoft Agents League Hackathon.

The project is designed for sustainability, sourcing, procurement, and business analytics teams that need to review supplier ESG data and identify risk drivers in a clear, explainable way.

## 2. Problem

Supplier sustainability review is often manual and inconsistent. Teams may need to review emissions, labor, waste, water, certification, audit recency, and supplier notes across many records.

Without a structured reasoning process, it can be difficult to identify which suppliers need urgent follow-up and why.

## 3. Solution

GreenChain IQ reviews synthetic supplier ESG data, classifies each supplier as Low, Medium, or High Risk, explains the risk drivers, retrieves relevant policy guidance, and recommends follow-up actions.

The project demonstrates a retrieval-grounded reasoning pattern designed for Foundry IQ integration.

## 4. Microsoft IQ Layer

The intended Microsoft IQ layer is Foundry IQ.

The current MVP includes synthetic policy documents and a local retrieval scaffold that mirrors the intended Foundry IQ pattern:

Supplier ESG data → risk drivers → relevant policy guidance → grounded recommendations.

The next integration phase connects these synthetic policy documents to Foundry IQ as a grounded knowledge base for the Microsoft Foundry reasoning agent.

## 5. Demo Walkthrough

First, I run the command-line demo:

```bash
python src/app.py
```

The app loads the synthetic supplier dataset and evaluates each supplier across emissions, labor, waste, water, certification status, and audit recency.

The demo produces a portfolio-level summary showing the number of High, Medium, and Low Risk suppliers.

It then prints detailed supplier-level reports with:

* Risk level
* Step-by-step reasoning
* Recommended actions
* Executive summary
* Grounded policy guidance from the synthetic knowledge documents

## 6. Example Result

For Metro Components, the agent classifies the supplier as High Risk because:

* Water score is below the high-risk threshold
* Certification is missing
* Last audit is older than the 12-month refresh window
* Multiple ESG scores are below 65

The agent recommends requesting updated certification, scheduling an updated supplier sustainability audit, requesting a water usage reduction plan, and adding the supplier to high-priority review.

## 7. Responsible AI and Data Safety

This project uses only synthetic demo data.

It does not include confidential employer, client, vendor, or personal information.

The agent is designed as a decision-support tool. It does not replace human compliance, legal, procurement, or sustainability review.

## 8. Closing

GreenChain IQ demonstrates how reasoning agents can support enterprise sustainability analytics by combining structured data evaluation, grounded knowledge retrieval, explainable recommendations, and responsible AI safeguards.
