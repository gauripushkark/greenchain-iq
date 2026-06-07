# Supplier Sustainability Risk Scoring Guide

## Purpose

This guide defines the scoring logic used to classify supplier sustainability risk as Low, Medium, or High.

The scoring model is designed for demonstration purposes using synthetic data. It should not be treated as a final compliance or procurement decision model.

## ESG Score Categories

Each supplier is evaluated across four sustainability score categories:

* Emissions Score
* Labor Score
* Waste Score
* Water Score

Scores range from 0 to 100, where higher scores indicate stronger sustainability performance.

## High-Risk Conditions

A supplier should be classified as High Risk if any of the following conditions are present:

* Any ESG score is below 50.
* Certification status is missing.
* The most recent audit is older than 12 months.
* Multiple ESG scores are below 65.
* Notes indicate serious unresolved sustainability issues.

## Medium-Risk Conditions

A supplier should be classified as Medium Risk if any of the following conditions are present and no high-risk condition applies:

* One or more ESG scores are between 50 and 64.
* Certification status is pending.
* Audit information is approaching the 12-month refresh window.
* Notes indicate incomplete improvement plans.
* The supplier has moderate sustainability gaps requiring follow-up.

## Low-Risk Conditions

A supplier may be classified as Low Risk if all of the following conditions are met:

* All ESG scores are 75 or higher.
* Certification status is valid.
* The most recent audit is within the past 12 months.
* Notes do not indicate unresolved sustainability issues.

## Recommended Reasoning Approach

The agent should explain the risk classification by identifying the most important risk drivers first. The explanation should be specific, evidence-based, and easy for business stakeholders to understand.
