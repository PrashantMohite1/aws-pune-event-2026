# AWS Kiro Crew — Learning Notes

## 1. What is AWS Kiro Crew?

Kiro Crew is an open-source, AI-powered development workspace designed to help coordinate AI agents and development tasks while maintaining project context across sessions.

It helps developers use AI to plan tasks, develop code, review implementations, and coordinate engineering workflows.

**Important:** Kiro Crew is a development tool, not an AWS infrastructure service like EC2, Lambda, or S3.

### Kiro Crew vs. Kiro IDE

- **Kiro Crew:** Focuses on coordinating development work and AI agents in a persistent workspace.
- **Kiro IDE:** An AI-powered code editor used to write, understand, and debug code.

Official resources:
- Kiro Crew: https://github.com/kirodotdev/KiroCrew
- Kiro IDE: https://kiro.dev/ide/

## 2. Can I practise Kiro Crew?

Yes. I can practise on my Windows laptop and use it to build real DevOps automation projects.

Potential learning areas:
- AI agent coordination
- Task planning and delegation
- Project context and instructions
- AI-assisted coding
- Code review and debugging
- Automated testing
- Git-based development workflows
- DevOps automation using Python and AWS

Follow the official repository's current installation instructions for Windows.

## 3. Practical Project: AWS EC2 Inventory Automation

### Objective

Build a Python application that retrieves EC2 instance information from AWS and displays an inventory report.

### Technologies

- Kiro Crew
- Python
- AWS boto3
- AWS CLI
- Git
- pytest

### Project Requirements

1. Accept an AWS region as input.
2. List EC2 instances in the selected region.
3. Display instance ID, name, state, instance type, and availability zone.
4. Handle missing instance-name tags.
5. Handle AWS API errors gracefully.
6. Add structured logging and appropriate exit codes.
7. Write unit tests using mocked AWS responses.
8. Create a README with setup instructions and example output.
9. Never hardcode AWS credentials.
10. Do not modify AWS resources.

### Proposed AI Agent Responsibilities

**Agent 1 — Planner**
- Understand the requirements.
- Break the project into smaller tasks.
- Propose the application structure.

**Agent 2 — Developer**
- Implement the Python application.
- Use boto3 to retrieve EC2 information.
- Follow Python coding best practices.

**Agent 3 — Reviewer**
- Review the generated code.
- Identify security and reliability issues.
- Check error handling and test coverage.

These are proposed responsibilities for learning; the actual agent configuration depends on the capabilities supported by Kiro Crew.

## 4. Practice Prompt

Paste the following prompt into the development workspace:

I am a DevOps engineer learning AI-assisted development.

Help me build a Python-based AWS EC2 inventory tool using boto3.

Requirements:
1. List EC2 instances in a user-selected AWS region.
2. Display instance ID, name, state, instance type, and availability zone.
3. Handle missing tags and AWS API errors gracefully.
4. Add unit tests using mocked AWS responses.
5. Follow Python best practices, logging, and proper exit codes.
6. Never hardcode AWS credentials.
7. Do not start, stop, terminate, or modify any AWS resources.
8. First propose the requirements, design, and implementation tasks.
9. Ask for my review before implementing the code.
10. Explain each important design decision so I can learn.

Create a README with setup instructions and example output.

## 5. Learning Workflow

| Step | Activity | Expected outcome |
|---|---|---|
| 1 | Install Kiro Crew | Get the workspace running |
| 2 | Explore agent capabilities | Understand task coordination |
| 3 | Define project requirements | Learn task planning |
| 4 | Review the proposed design | Understand the architecture |
| 5 | Generate Python code | Practise AI-assisted development |
| 6 | Review the implementation | Learn code review and debugging |
| 7 | Run pytest tests | Validate functionality |
| 8 | Integrate Git and CI checks | Apply DevOps practices |
| 9 | Document the project | Create a reusable portfolio project |

## 6. AWS Security Best Practices

- Start with mocked AWS responses to avoid unnecessary AWS access.
- Use a dedicated IAM identity with read-only permissions for EC2 inventory.
- Use AWS CLI profiles or another supported credential provider instead of hardcoded credentials.
- Never commit credentials or secret files to Git.
- Review AI-generated code before executing it.
- Check AWS region and account before running real AWS commands.

## 7. What I Should Learn from This Project

By completing this project, I should understand:

- How AI can assist with software development.
- How to break engineering work into smaller tasks.
- How to review and validate AI-generated code.
- How to use Python and boto3 for AWS automation.
- How to write tests and handle errors.
- How to apply security practices to AI-assisted DevOps workflows.

## 8. Next-Level Projects

After completing the EC2 inventory tool, I can try:

1. **S3 Inventory Tool:** List buckets, regions, versioning status, and encryption configuration.
2. **Terraform Code Reviewer:** Review Terraform changes for common security and configuration issues.
3. **Kubernetes Troubleshooting Assistant:** Analyse collected pod events and logs to suggest potential causes.
4. **CI/CD Pipeline Assistant:** Help create and test Jenkins pipeline definitions.

### Final Takeaway

Kiro Crew is worth exploring as a way to practise AI-assisted engineering. The goal is not just to generate code, but to learn how to plan work, coordinate AI assistance, validate results, and build reliable DevOps automation.
