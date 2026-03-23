---
name: Oracle Agent Spec Expert
description: Design framework-agnostic AI agents using Oracle's Open Agent Specification for portable, interoperable agentic systems with JSON/YAML definitions
version: 1.1.0
last_updated: 2026-01-06
external_version: "Agent Spec 1.0"
---

# Oracle Agent Spec Expert Skill

## Purpose
Master Oracle's Open Agent Specification (Agent Spec) to design framework-agnostic, declarative AI agents that can be authored once and deployed across multiple frameworks and runtimes.

## What is Agent Spec?

### Open Agent Specification
Framework-agnostic declarative language for defining agentic systems, building blocks for standalone agents and structured workflows, plus composition patterns for multi-agent systems.

**Key Innovation:** Decouple design from execution - write agents once, run anywhere.

**Release:** Technical report published October 2025 (arXiv:2510.04173)

## Core Philosophy

**The Problem:** Fragmented agent development - each framework requires different implementation.

**The Solution:** Unified representation - Agent Spec defines structure and behavior in JSON/YAML that any compatible runtime can execute.

**Benefit:** Author agents once → Deploy across frameworks → Reduce redundant development.

## Architecture

### Component Model
Agent Spec defines **conceptual building blocks** (components) that make up agent-based systems.

**Key Property:** All components are trivially serializable to JSON/YAML.

### Core Components

#### 1. LLMNode
**Purpose:** Text generation via LLM

**Definition:**
```yaml
type: LLMNode
name: "text_generator"
model: "claude-sonnet-4-5"
system_prompt: "You are a helpful assistant"
temperature: 0.7
max_tokens: 2000
```

#### 2. APINode
**Purpose:** External API calls

**Definition:**
```yaml
type: APINode
name: "weather_api"
endpoint: "https://api.weather.com/v1/current"
method: "GET"
parameters:
  location: "{input.location}"
headers:
  Authorization: "Bearer {env.API_KEY}"
```

#### 3. AgentNode
**Purpose:** Multi-round conversational agent

**Definition:**
```yaml
type: AgentNode
name: "support_agent"
model: "gpt-4"
system_prompt: "You are a customer support specialist"
tools:
  - type: function
    name: "lookup_order"
  - type: function
    name: "process_refund"
```

#### 4. WorkflowNode
**Purpose:** Orchestrate sequence of nodes

**Definition:**
```yaml
type: WorkflowNode
name: "data_pipeline"
steps:
  - node: extract_node
  - node: transform_node
  - node: load_node
error_handling: retry
```

## Agent Specification Format

### Basic Agent
```json
{
  "version": "1.0",
  "agent": {
    "name": "CustomerSupportAgent",
    "description": "Handles customer inquiries and support requests",
    "components": {
      "classifier": {
        "type": "LLMNode",
        "model": "claude-haiku-4",
        "system_prompt": "Classify customer inquiry type",
        "output": "inquiry_type"
      },
      "technical_support": {
        "type": "AgentNode",
        "model": "claude-sonnet-4-5",
        "tools": ["diagnose_issue", "escalate_ticket"]
      },
      "billing_support": {
        "type": "AgentNode",
        "model": "gpt-4",
        "tools": ["lookup_invoice", "process_refund"]
      },
      "router": {
        "type": "ConditionalNode",
        "conditions": [
          {
            "if": "inquiry_type == 'technical'",
            "then": "technical_support"
          },
          {
            "if": "inquiry_type == 'billing'",
            "then": "billing_support"
          }
        ]
      }
    },
    "entry_point": "classifier"
  }
}
```

### Multi-Agent System
```yaml
version: "1.0"
system:
  name: "ResearchSystem"
  description: "Multi-agent research and analysis system"

  agents:
    researcher:
      type: AgentNode
      model: claude-sonnet-4-5
      tools:
        - web_search
        - fetch_document
      system_prompt: "Research topics thoroughly"

    analyzer:
      type: AgentNode
      model: gpt-4o
      tools:
        - analyze_data
        - generate_insights
      system_prompt: "Analyze research findings"

    synthesizer:
      type: AgentNode
      model: claude-sonnet