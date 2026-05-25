
   Multimodal Compliance RAG Agent

 Project Overview
The Multimodal Compliance RAG Agent is an automated Video Compliance QA Pipeline. It leverages a Retrieval-Augmented Generation (RAG) architecture to audit video content against complex regulatory standards. By combining LLM-based reasoning with enterprise-grade cloud telemetry, this system transforms unstructured video data into structured, actionable compliance reports.
<img width="1594" height="969" alt="image" src="https://github.com/user-attachments/assets/d739c6c4-329b-452f-90fe-0d65e1278cdc" />


Architecture & Tech Stack
* **Orchestration:** LangGraph (Stateful multi-agent workflows)
* **LLM Engine:** Azure OpenAI (GPT-4o)
* **Multimodal Ingestion:** Azure Video Indexer (Transcript & OCR analysis)
* **Knowledge Base:** Azure AI Search (Vector search for compliance rules)
* **Embeddings:** OpenAI `text-embedding-3-small`
* **Observability:** Azure Application Insights & LangSmith
* **Language:** Python

Key Features
* **Automated Compliance Auditing:** Deterministically detect violations in video content.
* **Multimodal Retrieval:** Processes both transcripts and visual text (OCR) via Video Indexer.
* **Production-Grade Telemetry:** Full-stack monitoring with Application Insights.
* **Stateful Reasoning:** Complex, multi-step validation logic orchestrated via LangGraph.
* <img width="740" height="670" alt="image" src="https://github.com/user-attachments/assets/104eacbe-e523-4a8f-be9b-178248831ca4" />


Prerequisites
* Python 3.10+
* Azure Subscription (OpenAI, AI Search, Video Indexer)
* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured

 (Key Features)
1.Automated Multimodal Auditing: Uses Azure Video Indexer to analyze both transcripts and visual text (OCR) against regulatory standards simultaneously.

2.RAG-Powered Accuracy: Retrieves specific compliance documentation via Azure AI Search to ensure decisions are grounded in facts, not hallucinations.

3.Full-Stack Observability: Integrates LangSmith and Azure Application Insights to provide a transparent, step-by-step audit trail for every decision the AI makes.

4.Stateful Orchestration: Utilizes LangGraph to handle complex, multi-step verification workflows without human intervention
