# /build-rag - Build RAG System with OCI GenAI Agents

## Context
Design and implement a RAG system using OCI GenAI Agents.

## Workflow

### 1. Requirements
- **Data sources**: OCI Object Storage, databases?
- **Volume**: Document count, update frequency?
- **Query patterns**: Semantic, keyword, hybrid?
- **Languages**: Multi-lingual support needed?

### 2. Architecture

```
┌──────────────────────────────────────────────────────────┐
│                   OCI GenAI Agents                        │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  Documents ──▶ Object Storage ──▶ Data Source             │
│                                        │                  │
│                                        ▼                  │
│                              Knowledge Base               │
│                             (OCI/OpenSearch)              │
│                                        │                  │
│                                        ▼                  │
│  User Query ──▶ Agent Endpoint ──▶ RAG Tool ──▶ Response  │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

### 3. Create Knowledge Base

```python
from oci.generative_ai_agent import GenerativeAiAgentClient

client = GenerativeAiAgentClient(config)

# Create knowledge base
kb = client.create_knowledge_base(
    CreateKnowledgeBaseDetails(
        compartment_id=COMPARTMENT_ID,
        display_name="enterprise-kb",
        index_config=OciOpenSearchIndexConfig(
            cluster_id=OPENSEARCH_CLUSTER_OCID,
            secret_id=SECRET_OCID
        )
    )
)
```

### 4. Create Data Source

```python
# Connect Object Storage
data_source = client.create_data_source(
    CreateDataSourceDetails(
        compartment_id=COMPARTMENT_ID,
        knowledge_base_id=kb.data.id,
        display_name="docs-source",
        data_source_config=OciObjectStorageDataSourceConfig(
            object_storage_prefixes=[
                ObjectStoragePrefix(
                    namespace=NAMESPACE,
                    bucket_name="documents",
                    prefix="knowledge/"
                )
            ]
        )
    )
)
```

### 5. Create Agent

```python
agent = client.create_agent(
    CreateAgentDetails(
        compartment_id=COMPARTMENT_ID,
        display_name="rag-agent",
        knowledge_base_ids=[kb.data.id],
        welcome_message="How can I help you today?"
    )
)
```

### 6. Test

```python
from oci.generative_ai_agent_runtime import GenerativeAiAgentRuntimeClient

runtime = GenerativeAiAgentRuntimeClient(config)

response = runtime.chat(
    agent_endpoint_id=ENDPOINT_OCID,
    chat_details=ChatDetails(
        user_message="What are the key policies?",
        session_id="test-session"
    )
)
print(response.data.message.content.text)
```

## Skills to Activate
- rag-expert
- genai-dac-specialist
- oracle-adk
