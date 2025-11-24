EmpathiAI – An Empathetic Dialogue System for Mental-Health Support
1. Project Overview

EmpathiAI is an artificial intelligence system designed to provide empathetic dialogue responses in mental-health support contexts.
The system generates empathetic responses to user text inputs and simultaneously performs multi-task predictions, including:

Empathy level classification

Risk level estimation

Detection of crisis-related linguistic cues

Assessment of self-awareness indicators

The system integrates multiple components, including a fine-tuned language model (e.g., RoBERTa / DeBERTa), structured diagnostic modeling via TabNet, and explainability through graph-based attention mechanisms (GNN/GAT).
Human-in-the-loop mechanisms are incorporated to enhance empathy expression quality and ensure safe, reliable decision-making.

This repository presents the full lifecycle of the system, including development, evaluation, documentation, and demonstration.

2. Repository Structure
EmpathiAI/
│
├── src/
│   ├── main.py                     # System entry point
│   ├── models/                     # Trained models or loading scripts
│   ├── utils/                      # Preprocessing, inference, and metrics
│   ├── data/                       # Sample input/output data
│   ├── __init__.py
│
├── deployment/                     # Not used (placeholder)
│   ├── Dockerfile
│
├── monitoring/                     # Not used (placeholder)
│   ├── prometheus/
│   ├── grafana/
│
├── documentation/
│   ├── AI-System-Project-Proposal.pdf
│   ├── Project-Report.pdf
│   ├── README.md (optional)
│
├── notebooks/
│   ├── model_development.ipynb
│   ├── privacy_scan.ipynb
│   ├── data_cleaning.ipynb
│   ├── trustworthiness_checks.ipynb
│
├── videos/
│   ├── system_demo.mp4
│
├── .gitignore
├── requirements.txt
└── README.md

3. System Entry Point (src/main.py)

EmpathiAI can be executed locally through the system entry script.

Single-input mode:
python src/main.py --text "I feel very stressed lately."


This returns a structured output including:

Generated empathetic response

Empathy score

Estimated risk level

Timestamped output automatically saved to src/data/sample_output.json

Interactive mode:
python src/main.py


Type exit or quit to terminate.

4. Demonstration Video

A demonstration of the system’s execution, response generation, and evaluation workflow is provided at:

videos/system_demo.mp4


The video illustrates:

Running the system using main.py

Generating empathetic responses

Producing risk-related indicators

(If applicable) displaying explainability or human-in-the-loop rewriting steps

5. Deployment Strategy

This project is implemented as a local research prototype.
Containerization (Docker/Kubernetes) is not used for this version because:

The system is not deployed as a persistent service

Real-time serving and API hosting are not required for the scope of the course

Local execution sufficiently demonstrates model functionality and workflow

The deployment/ folder is included as a placeholder for potential future extensions.

6. Monitoring and Metrics

Prometheus and Grafana are not used in this project.
The system does not operate as an online, continuously running service; therefore, real-time monitoring is not necessary.

Instead, all evaluation is performed offline through the included notebooks:

Model performance

Calibration and reliability analysis

Trustworthiness and fairness checks

Privacy and risk analysis

Relevant files are located in the notebooks/ directory.

7. Project Documentation

All project documentation is provided in the documentation/ directory:

AI-System-Project-Proposal.pdf

Project-Report.pdf (or placeholder if still under development)

These documents describe the system goals, architecture, risk integration, evaluation, and design rationale.

8. Version Control and Collaboration Practices

This repository uses standard version control practices:

Main branch contains the stable submission version.

Development branch (if used) contains experimental or iterative updates.

Commit messages record changes related to model development, data processing, risk analysis, and documentation.

Large model checkpoints are excluded using .gitignore to maintain repository size.

9. Components Not Used in This Project

The following components are not included in this implementation:

Containerization (Docker / Kubernetes)

Not required for the project scope; execution is local.

Monitoring stacks (Prometheus / Grafana)

Not applicable because the system does not run as a live service.

Multi-container orchestration

Not needed due to the single-process nature of the prototype.

10. Reproduction Instructions
1. Clone the repository:
git clone https://github.com/<your-username>/<your-repo>.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the system:
python src/main.py --text "I feel sad and anxious recently."

11. Acknowledgments

This repository was created as part of
Machine Learning for AI Systems — Final Project
University of Florida, Fall 2025.

The work reflects principles of trustworthy AI development, responsible risk integration, and human-centered model design.
