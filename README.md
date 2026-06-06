# Multi-Agent Customer Feedback Processing with Microsoft Agent Framework

This project demonstrates how to build a multi-agent workflow using the Microsoft Agent Framework and the Sequential Orchestration pattern.

The solution processes customer feedback through a pipeline of specialized AI agents, where each agent is responsible for a specific task:

* **Summarizer Agent** – Converts raw customer feedback into a short, neutral summary.
* **Classifier Agent** – Categorizes the feedback as **Positive**, **Negative**, or **Feature Request**.
* **Recommended Action Agent** – Suggests an appropriate follow-up action based on the summary and classification.

By chaining agents together, the workflow showcases how complex business processes can be broken down into smaller, focused responsibilities. This approach improves maintainability, reusability, and scalability compared to using a single agent for all tasks.

## Features

* Multi-agent architecture using Microsoft Agent Framework
* Sequential orchestration of agent interactions
* Customer feedback analysis and categorization
* Actionable recommendations for support and product teams
* Azure AI integration for agent execution
* Async workflow execution using Python

## Example Workflow

**Input:**
Customer feedback describing an issue, compliment, or enhancement request.

**Output:**

1. Feedback summary
2. Classification (Positive, Negative, or Feature Request)
3. Recommended next action

## Learning Objectives

* Create and configure AI agents using Microsoft Agent Framework
* Implement sequential orchestration patterns
* Design task-specific agent instructions
* Pass outputs between multiple agents
* Build AI-powered business process automation workflows

This project serves as a practical introduction to multi-agent systems and demonstrates how AI agents can collaborate to transform unstructured customer feedback into meaningful business insights and recommended actions.

## Test Run - Output

<img width="850" height="705" alt="image" src="https://github.com/user-attachments/assets/8713454c-11a8-466c-93ee-628718d0df5b" />

## .env

Needs two variables:
- AZURE_PROJECT_ENDPOINT = your-project-link
- MODEL_DEPLOYMENT_NAME = model-deployment


## Miscellaneous

<br><br>

<img width="1399" height="836" alt="edges" src="https://github.com/user-attachments/assets/785882a5-4615-4eb8-8cc4-f6510789c122" />

<br><br>

<img width="1758" height="806" alt="patterns" src="https://github.com/user-attachments/assets/d258d404-da91-4630-a0e1-3069da4ddba7" />

<br><br>

<img width="1764" height="739" alt="steps" src="https://github.com/user-attachments/assets/0a8a6889-d454-4493-9f3c-7dab6167064d" />
