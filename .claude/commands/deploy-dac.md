# /deploy-dac - Deploy OCI Dedicated AI Cluster

## Context
Deploy an Oracle Cloud Infrastructure GenAI Dedicated AI Cluster.

## Prerequisites
- OCI tenancy with GenAI service enabled
- Compartment with proper IAM policies
- OCI CLI configured or Terraform auth set up

## Workflow

### 1. Gather Requirements
- **Use case**: Hosting only or Fine-tuning needed?
- **Model**: Cohere Command R+/R/Light or Meta Llama?
- **Traffic**: Expected requests/minute
- **Region**: Check availability (US Midwest Chicago, UK South London, Germany Central Frankfurt)

### 2. Size the Cluster

| Workload | Units | Monthly Cost | Throughput |
|----------|-------|--------------|------------|
| Dev/Test | 2-5 | $3-7.5K | ~50-125 RPM |
| Production | 5-15 | $7.5-22.5K | ~125-375 RPM |
| High Volume | 15-30 | $22.5-45K | ~375-750 RPM |
| Enterprise | 30-50 | $45-75K | ~750-1250 RPM |

### 3. Deploy

#### Option A: Terraform (Recommended)
```bash
cd templates/terraform/oci-genai-dac
terraform init
terraform plan -var="compartment_id=ocid1.compartment..."
terraform apply
```

#### Option B: OCI CLI
```bash
oci generative-ai dedicated-ai-cluster create \
  --compartment-id $COMPARTMENT_ID \
  --unit-count 5 \
  --unit-shape LARGE_COHERE \
  --display-name "production-dac"
```

### 4. Create Endpoint
```bash
oci generative-ai endpoint create \
  --compartment-id $COMPARTMENT_ID \
  --dedicated-ai-cluster-id $DAC_OCID \
  --model-id cohere.command-r-plus \
  --display-name "prod-endpoint"
```

### 5. Post-Deployment Checklist
- [ ] Verify endpoint health
- [ ] Configure monitoring (OCI Monitoring)
- [ ] Set up alarms for unit utilization
- [ ] Tag resources for cost tracking
- [ ] Test inference latency
- [ ] Document endpoint OCIDs

## Skills to Activate
- genai-dac-specialist
- oci-services-expert
