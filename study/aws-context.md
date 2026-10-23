# AWS Context – Notes

## 1. What is AWS Context?

AWS Context is an AWS capability designed to help AI agents understand relationships between enterprise data, business concepts, systems, and organizational rules.

It provides relevant context so AI agents can retrieve information and answer questions more accurately.

**In simple words:** AWS Context helps AI agents understand how different pieces of company information are connected.

## 2. Why Do We Need AWS Context?

Organizations store information across multiple systems, such as:
- Databases
- Documents
- Cloud infrastructure
- Monitoring dashboards
- Business applications
- Operational runbooks

An AI agent may retrieve information from these sources but lack an understanding of how the information relates to each other.

AWS Context aims to help solve this problem by providing structured, connected, and governed context.

## 3. How Does AWS Context Work?

1. Enterprise data exists across different sources.
2. Relationships between data, systems, and business concepts are established.
3. Relevant context is made available to AI agents.
4. AI agents use that context to answer questions or perform tasks.
5. Access controls and governance help ensure that information is used appropriately.

*Note: The exact workflow depends on the service's supported integrations and configuration.*

## 4. Real-World Example

Suppose a company wants to understand why its AWS bill has increased.

Without sufficient context:
- An AI agent examines a billing report.
- It identifies an increase in EC2 costs.
- It may not know which application or business team owns those instances.

With connected contextual information:
- The agent can relate EC2 instances to applications.
- It can identify the owning team and relevant cost-allocation rules.
- It can provide a more useful explanation of the increase.

The quality of the result depends on the data sources, available relationships, and permissions configured.

## 5. Key Concepts

- **Context:** Information that helps an AI agent understand a situation.
- **Knowledge graph:** A representation of entities and their relationships.
- **AI agent:** Software that uses AI to reason, retrieve information, and perform tasks.
- **Governance:** Rules that control access to and use of information.
- **Enterprise data:** Information stored across an organization's systems.

## 6. AWS Context vs Amazon Bedrock vs Kiro

### AWS Context
Provides connected organizational context to help AI agents understand enterprise information.

### Amazon Bedrock
AWS platform for building generative AI applications and AI agents using supported foundation models and services.

### Kiro
An AI-powered development environment that helps developers plan, write, test, and improve code.

**Remember:**
- AWS Context = Organizational context for AI agents.
- Amazon Bedrock = Platform for building generative AI applications.
- Kiro = AI-assisted software development.

These products have different purposes and should not be treated as interchangeable.

## 7. DevOps Use Cases

AWS Context could be useful in scenarios such as:

1. **Incident investigation:** Relate an application to its infrastructure, logs, and runbooks.
2. **Cloud cost analysis:** Connect resource costs to applications and owning teams.
3. **Infrastructure understanding:** Help an AI agent understand relationships between AWS resources.
4. **Troubleshooting:** Provide relevant deployment documentation and operational procedures.
5. **Knowledge retrieval:** Help teams find information distributed across organizational systems.

These are potential application scenarios, not a guarantee that every use case is supported out of the box.

## 8. Hands-On Practice Idea

Build a basic AI-powered DevOps assistant that can answer:

- Which AWS resources belong to a particular application?
- What should I check when an EC2 instance becomes unhealthy?
- Which runbook explains a particular incident?
- Which application is associated with a particular infrastructure resource?

Possible learning components:
- AWS resource metadata
- CloudWatch logs and metrics
- Operational documentation
- An AI application or agent
- Appropriate IAM permissions and access controls

Start with a small prototype using documented, available AWS services. Verify AWS Context's current availability and supported integrations before attempting a direct integration.

## 9. Interview Answer

**Question: What is AWS Context?**

AWS Context is an AWS capability designed to provide AI agents with relevant enterprise context by connecting information, relationships, and business concepts across organizational data sources. This helps agents understand how information relates to each other and produce more relevant answers while respecting configured access controls.

## 10. Quick Revision

- AWS Context helps AI agents understand connected enterprise information.
- It focuses on context and relationships rather than simply retrieving isolated documents.
- Knowledge graphs can represent relationships between entities.
- Amazon Bedrock is used to build generative AI applications and agents.
- Kiro supports AI-assisted software development.
- DevOps applications may include incident investigation, infrastructure analysis, and cloud cost analysis.
- Always verify current service availability and supported integrations using official AWS documentation.

Official AWS reference:
https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/
