# Agent Orchestration Design

## Purpose

This document describes the logical multi-agent orchestration design for GreenChain IQ.

GreenChain IQ is a sustainability certification readiness reasoning-agent MVP. It evaluates synthetic supplier ESG data, retrieves grounded policy guidance, classifies supplier readiness risk, recommends follow-up actions, and generates business-ready summaries.

The current MVP is implemented as a command-line prototype with modular Python logic. The design is structured as a multi-agent workflow so it can later be expanded into Microsoft Foundry Agent Service or Microsoft Agent Framework.

## Multi-Agent Workflow

GreenChain IQ is designed around five logical agents:

1. Supplier Data Review Agent
2. Certification Readiness Agent
3. Grounded Policy Retrieval Agent
4. Corrective Action Recommendation Agent
5. Executive Summary Agent

## 1. Supplier Data Review Agent

### Responsibility

The Supplier Data Review Agent reviews the synthetic supplier ESG dataset and validates whether key fields are present and usable.

### Inputs

* Supplier name
* Region
* Emissions score
* Labor score
* Waste score
* Water score
* Certification status
* Last audit date
* Supplier notes

### Outputs

* Validated supplier record
* Missing or invalid data flags
* ESG score observations
* Audit recency observations
* Certification status observations

## 2. Certification Readiness Agent

### Responsibility

The Certification Readiness Agent evaluates supplier sustainability certification readiness based on the validated supplier data.

### Reasoning Steps

1. Check whether any ESG score is below the high-risk threshold.
2. Check whether multiple ESG scores are below the preferred threshold.
3. Check whether certification is missing or pending.
4. Check whether the latest audit is older than the 12-month refresh window.
5. Classify the supplier as Low, Medium, or High Risk.

### Outputs

* Risk classification
* Key risk drivers
* Structured reasoning explanation

## 3. Grounded Policy Retrieval Agent

### Responsibility

The Grounded Policy Retrieval Agent retrieves relevant policy guidance from synthetic knowledge documents.

### Current MVP Implementation

The current MVP uses a local retrieval scaffold that reads markdown files from the `docs/` folder and selects relevant documents based on risk drivers.

### Planned Foundry IQ Implementation

In the planned Microsoft Foundry implementation, the synthetic policy documents would be connected to a Foundry IQ knowledge base. The agent would retrieve relevant grounded guidance from Foundry IQ before generating recommendations.

### Knowledge Sources

* `supplier_esg_policy.md`
* `risk_scoring_guide.md`
* `certification_requirements.md`
* `audit_frequency_rules.md`
* `corrective_action_playbook.md`

### Outputs

* Relevant policy guidance
* Source document names
* Grounding context for recommendations

## 4. Corrective Action Recommendation Agent

### Responsibility

The Corrective Action Recommendation Agent recommends supplier follow-up actions based on the risk classification, risk drivers, and grounded policy guidance.

### Example Recommendations

* Request updated sustainability certification.
* Schedule an updated supplier sustainability audit.
* Request a water usage reduction plan.
* Request a waste reduction or recycling improvement plan.
* Add supplier to high-priority sustainability review.
* Add supplier to quarterly monitoring.
* Continue standard annual supplier sustainability monitoring.

### Outputs

* Prioritized follow-up actions
* Action rationale tied to risk drivers

## 5. Executive Summary Agent

### Responsibility

The Executive Summary Agent converts the detailed risk analysis into a concise business-ready summary for stakeholders.

### Outputs

* Supplier-level executive summary
* Portfolio-level risk summary
* Responsible AI and data safety note

## End-to-End Orchestration Flow

```text
User / Business Analyst
  → Supplier Data Review Agent
  → Certification Readiness Agent
  → Grounded Policy Retrieval Agent
  → Corrective Action Recommendation Agent
  → Executive Summary Agent
  → Business-ready supplier certification readiness report
```

## Current MVP Mapping

The current Python MVP maps to the logical agents as follows:

| Logical Agent                          | Current MVP File        |
| -------------------------------------- | ----------------------- |
| Supplier Data Review Agent             | `src/risk_scoring.py`   |
| Certification Readiness Agent          | `src/risk_scoring.py`   |
| Grounded Policy Retrieval Agent        | `src/knowledge_base.py` |
| Corrective Action Recommendation Agent | `src/risk_scoring.py`   |
| Executive Summary Agent                | `src/app.py`            |

## Responsible AI and Safety Design

GreenChain IQ follows these safety principles:

* Uses synthetic demo data only.
* Does not include confidential employer, client, vendor, customer, employee, or personal information.
* Does not store secrets, credentials, or API keys.
* Provides explanations for risk classifications.
* Treats outputs as decision support, not final compliance, legal, procurement, or sustainability decisions.
* Makes missing or incomplete data visible instead of guessing.

## Future Foundry Implementation

Future implementation steps include:

1. Create a Microsoft Foundry project.
2. Connect the synthetic policy documents to Foundry IQ.
3. Configure a Microsoft Foundry agent with GreenChain IQ instructions.
4. Connect the agent to the Foundry IQ knowledge base.
5. Add source citations from retrieved policy guidance.
6. Add evaluations for risk classification accuracy and grounding quality.
7. Optionally split the logical agents into separate Microsoft Agent Framework components.
