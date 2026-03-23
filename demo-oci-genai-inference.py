#!/usr/bin/env python3
"""
OCI GenAI Inference Demo Script

This demonstrates basic text generation using OCI Generative AI Service
with Cohere Command R+ model on a Dedicated AI Cluster (DAC).

Requirements:
- OCI CLI configured (oci config)
- Python 3.10+
- oci package: pip install oci
- Valid OCI compartment and DAC endpoint

Usage:
python demo-oci-genai-inference.py
"""

import oci
from oci.generative_ai_inference import GenerativeAiInferenceClient
from oci.generative_ai_inference.models import (
    CohereLlmInferenceRequest,
    DedicatedServingMode,
    GenerateTextDetails
)

# Configuration
COMPARTMENT_ID = "ocid1.compartment.oc1..your_compartment_id_here"
ENDPOINT_ID = "ocid1.generativeaiendpoint.oc1..your_endpoint_id_here"

def main():
    # Load OCI configuration
    config = oci.config.from_file()

    # Initialize client
    client = GenerativeAiInferenceClient(config)

    # Prepare inference request
    prompt = """
    As an OCI AI Architect, explain the benefits of using Dedicated AI Clusters
    for enterprise AI workloads. Include cost optimization strategies and
    production deployment patterns.
    """

    inference_request = CohereLlmInferenceRequest(
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        top_k=50,
        top_p=0.9
    )

    # Create generation request for DAC endpoint
    generate_text_details = GenerateTextDetails(
        compartment_id=COMPARTMENT_ID,
        serving_mode=DedicatedServingMode(endpoint_id=ENDPOINT_ID),
        inference_request=inference_request
    )

    try:
        print("Sending inference request to OCI GenAI DAC...")
        print(f"Prompt: {prompt[:100]}...")
        print("-" * 50)

        # Execute inference
        response = client.generate_text(generate_text_details)

        # Extract and display results
        generated_text = response.data.inference_response.generated_texts[0].text
        token_count = response.data.inference_response.generated_texts[0].token_likelihoods

        print("Generated Response:")
        print(generated_text)
        print("-" * 50)
        print(f"Total tokens used: {len(token_count)}")

    except oci.exceptions.ServiceError as e:
        print(f"OCI Service Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()