# GreenChain IQ Sample Output

This file shows sample output from the command-line MVP demo.

Command used:

```bash
python src/app.py
================================================================================
GreenChain IQ: Supplier Sustainability Risk Agent
================================================================================

Project Purpose:
GreenChain IQ helps evaluate supplier sustainability risk using synthetic ESG data and grounded policy guidance.

Hackathon Track:
Reasoning Agents

Microsoft IQ Layer:
Foundry IQ

Demo Question:
Analyze the supplier sustainability dataset and identify which suppliers are
High Risk. Explain the reasoning and recommend prioritized follow-up actions.

System Prompt Preview:
You are GreenChain IQ, a supplier sustainability risk reasoning agent.

Your role is to help sustainability, sourcing, procurement, and business
analytics teams evaluate supplier ESG risk using synthetic supplier data and
grounded policy guidance from a Foundry IQ knowledge base.

You must follow these principles:

1. Use structured reasoning.
   Evaluate supplier risk step by step:
   - Review supplier ESG scores.
   - Check certification status.
   - Check audit recency.
   - Identify missing or incomplete information.
   - Retrieve relevant policy guidance.
   - Classify supplier risk.
   - Recommend follow-up actions.

2. Ground your recommendations.
   Use retrieved policy, scoring, cer
...

================================================================================
Portfolio-Level Risk Summary
================================================================================
High Risk Suppliers: 4
Medium Risk Suppliers: 1
Low Risk Suppliers: 3

High Risk Supplier List:
- Metro Components
- Nova Packaging
- Riverbend Plastics
- BlueRiver Components

================================================================================
Detailed Supplier Risk Reports
================================================================================

================================================================================
Supplier: GreenParts Co.
Risk Level: Low

Reasoning:
1. Supplier meets the low-risk criteria based on available synthetic ESG data.

Recommended Actions:
- Continue standard annual supplier sustainability monitoring.

Executive Summary:
GreenParts Co. is classified as Low Risk based on the synthetic ESG review. The main drivers are: Supplier meets the low-risk criteria based on available synthetic ESG data.
================================================================================

Grounded Policy Guidance:
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: supplier_esg_policy.md
  Guidance: This policy defines the sustainability expectations for suppliers included in the supplier risk review process. The goal is to support responsible sourcing decisions by evaluating environmental, labor, waste, water, certification, and audit-related risk factors.

================================================================================
Supplier: Metro Components
Risk Level: High

Reasoning:
1. Water score is 44, which is below the high-risk threshold of 50.
2. Certification status is missing, which requires supplier documentation follow-up.
3. Last audit date is 2024-11-12, which is older than the 12-month refresh window.
4. 3 ESG scores are below 65, indicating multiple sustainability gaps.

Recommended Actions:
- Request updated sustainability or environmental certification.
- Schedule an updated supplier sustainability audit.
- Request a water usage reduction plan.
- Add supplier to high-priority sustainability review.
- Add supplier to quarterly monitoring.

Executive Summary:
Metro Components is classified as High Risk based on the synthetic ESG review. The main drivers are: Water score is 44, which is below the high-risk threshold of 50. Certification status is missing, which requires supplier documentation follow-up.
================================================================================

Grounded Policy Guidance:
- Source: certification_requirements.md
  Guidance: This document defines certification expectations for suppliers included in the sustainability risk review process.
- Source: audit_frequency_rules.md
  Guidance: This document defines audit recency expectations for suppliers included in the sustainability risk review process.
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: corrective_action_playbook.md
  Guidance: This playbook defines recommended follow-up actions for suppliers identified as Medium Risk or High Risk during sustainability review.
- Source: supplier_esg_policy.md
  Guidance: This policy defines the sustainability expectations for suppliers included in the supplier risk review process. The goal is to support responsible sourcing decisions by evaluating environmental, labor, waste, water, certification, and audit-related risk factors.

================================================================================
Supplier: Nova Packaging
Risk Level: High

Reasoning:
1. Waste score is 48, which is below the high-risk threshold of 50.
2. Certification status is pending and should be tracked until resolved.
3. Last audit date is 2025-05-20, which is older than the 12-month refresh window.

Recommended Actions:
- Follow up on pending certification status.
- Schedule an updated supplier sustainability audit.
- Request a waste reduction or recycling improvement plan.
- Add supplier to high-priority sustainability review.

Executive Summary:
Nova Packaging is classified as High Risk based on the synthetic ESG review. The main drivers are: Waste score is 48, which is below the high-risk threshold of 50. Certification status is pending and should be tracked until resolved.
================================================================================

Grounded Policy Guidance:
- Source: certification_requirements.md
  Guidance: This document defines certification expectations for suppliers included in the sustainability risk review process.
- Source: audit_frequency_rules.md
  Guidance: This document defines audit recency expectations for suppliers included in the sustainability risk review process.
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: corrective_action_playbook.md
  Guidance: This playbook defines recommended follow-up actions for suppliers identified as Medium Risk or High Risk during sustainability review.

================================================================================
Supplier: Bright Alloy Ltd.
Risk Level: Low

Reasoning:
1. Supplier meets the low-risk criteria based on available synthetic ESG data.

Recommended Actions:
- Continue standard annual supplier sustainability monitoring.

Executive Summary:
Bright Alloy Ltd. is classified as Low Risk based on the synthetic ESG review. The main drivers are: Supplier meets the low-risk criteria based on available synthetic ESG data.
================================================================================

Grounded Policy Guidance:
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: supplier_esg_policy.md
  Guidance: This policy defines the sustainability expectations for suppliers included in the supplier risk review process. The goal is to support responsible sourcing decisions by evaluating environmental, labor, waste, water, certification, and audit-related risk factors.

================================================================================
Supplier: Riverbend Plastics
Risk Level: High

Reasoning:
1. Emissions score is 46, which is below the high-risk threshold of 50.
2. Certification status is missing, which requires supplier documentation follow-up.
3. Last audit date is 2024-08-18, which is older than the 12-month refresh window.
4. 4 ESG scores are below 65, indicating multiple sustainability gaps.

Recommended Actions:
- Request updated sustainability or environmental certification.
- Schedule an updated supplier sustainability audit.
- Add supplier to high-priority sustainability review.
- Add supplier to quarterly monitoring.

Executive Summary:
Riverbend Plastics is classified as High Risk based on the synthetic ESG review. The main drivers are: Emissions score is 46, which is below the high-risk threshold of 50. Certification status is missing, which requires supplier documentation follow-up.
================================================================================

Grounded Policy Guidance:
- Source: certification_requirements.md
  Guidance: This document defines certification expectations for suppliers included in the sustainability risk review process.
- Source: audit_frequency_rules.md
  Guidance: This document defines audit recency expectations for suppliers included in the sustainability risk review process.
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: corrective_action_playbook.md
  Guidance: This playbook defines recommended follow-up actions for suppliers identified as Medium Risk or High Risk during sustainability review.
- Source: supplier_esg_policy.md
  Guidance: This policy defines the sustainability expectations for suppliers included in the supplier risk review process. The goal is to support responsible sourcing decisions by evaluating environmental, labor, waste, water, certification, and audit-related risk factors.

================================================================================
Supplier: EcoFiber Manufacturing
Risk Level: Low

Reasoning:
1. Supplier meets the low-risk criteria based on available synthetic ESG data.

Recommended Actions:
- Continue standard annual supplier sustainability monitoring.

Executive Summary:
EcoFiber Manufacturing is classified as Low Risk based on the synthetic ESG review. The main drivers are: Supplier meets the low-risk criteria based on available synthetic ESG data.
================================================================================

Grounded Policy Guidance:
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: supplier_esg_policy.md
  Guidance: This policy defines the sustainability expectations for suppliers included in the supplier risk review process. The goal is to support responsible sourcing decisions by evaluating environmental, labor, waste, water, certification, and audit-related risk factors.

================================================================================
Supplier: Summit Textiles
Risk Level: Medium

Reasoning:
1. Certification status is pending and should be tracked until resolved.

Recommended Actions:
- Follow up on pending certification status.

Executive Summary:
Summit Textiles is classified as Medium Risk based on the synthetic ESG review. The main drivers are: Certification status is pending and should be tracked until resolved.
================================================================================

Grounded Policy Guidance:
- Source: certification_requirements.md
  Guidance: This document defines certification expectations for suppliers included in the sustainability risk review process.

================================================================================
Supplier: BlueRiver Components
Risk Level: High

Reasoning:
1. Emissions score is 49, which is below the high-risk threshold of 50.

Recommended Actions:
- Add supplier to high-priority sustainability review.

Executive Summary:
BlueRiver Components is classified as High Risk based on the synthetic ESG review. The main drivers are: Emissions score is 49, which is below the high-risk threshold of 50.
================================================================================

Grounded Policy Guidance:
- Source: risk_scoring_guide.md
  Guidance: This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.
- Source: corrective_action_playbook.md
  Guidance: This playbook defines recommended follow-up actions for suppliers identified as Medium Risk or High Risk during sustainability review.

================================================================================
Responsible AI and Data Safety Note
================================================================================
This demo uses only synthetic supplier data. It does not include confidential employer, client, vendor, or personal information.
The agent is designed as a decision-support tool and does not replace human compliance, legal, procurement, or sustainability review.

