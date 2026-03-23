# Skill Auto-Activation Hook for Cline

This hook analyzes user prompts and suggests relevant OCI skills based on `.cline/settings/skill-rules.json`.

## How It Works

When a user submits a prompt, this hook:
1. Scans for OCI-specific keywords
2. Matches intent patterns against the prompt
3. Suggests the most relevant OCI skill(s)

## OCI Skill Triggers

| Skill | Key Triggers |
|-------|--------------|
| oci-services-expert | OCI, Oracle Cloud, compartment, Vision, Speech |
| genai-dac-specialist | DAC, Dedicated AI Cluster, Cohere, Command R |
| oracle-adk | ADK, Agent Development Kit, function tools |
| oracle-agent-spec | agent specification, agent spec, portable agent |
| rag-expert | RAG, retrieval, knowledge base, GenAI Agents |
| mcp-architecture | MCP, Model Context Protocol, Oracle MCP |

## Usage

Skills activate automatically. To check which skills apply:

```bash
# Check skill match for a query (Cline CLI)
cline "What skills apply to: deploy a RAG system with OCI GenAI Agents"
```

## Customization

Edit `.cline/settings/skill-rules.json` to:
- Add new OCI-specific keywords
- Adjust intent patterns
- Create new skill triggers