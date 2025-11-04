# EmpathiAI-Data-Management
Data cleaning, risk management, and trustworthiness implementation for the EmpathiAI project.
EmpathiAI — Data Management & Risk Report

This repo includes data cleaning, risk matrix, and trustworthiness checks for the Mental Health Counseling Conversations dataset.
Supports Project Sections 5–6: Risk & Data Collection Management.

Structure
data/processed/           → cleaned CSVs
reports/trustworthiness_report.md
risk/risk_matrix.py, risk_matrix.png
src/cleaning.py
src/trustworthiness_checks.py
requirements.txt

Dataset

Source: tcabanski/mental_health_counseling_conversations_rated
Text data with empathy, appropriateness, and relevance scores.
Setup
pip install -r requirements.txt
 Data Cleaning
python src/cleaning.py

Combines context + response

Cleans text, removes duplicates
Splits 80/10/10 into train/val/test
Trustworthiness
python src/trustworthiness_checks.py
Generates a Markdown report with:
Missing data check
Outlier ratio (IQR)
Drift (KS test)
Rater consistency (Cronbach’s α)
Risk Matrix
python risk/risk_matrix.py
Creates risk_matrix.png (Likelihood × Impact visualization).
