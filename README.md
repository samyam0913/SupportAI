# SupportAI

**Multi-Tenant AI Customer Support SaaS Platform**

SupportAI is a production-oriented full-stack SaaS application that enables organizations to deploy an AI-powered customer support agent trained on their own knowledge base.

The project is designed as a software engineering portfolio project to demonstrate production-grade backend development, AI/RAG engineering, multi-tenant SaaS architecture, testing, observability, and DevOps practices.

## Features

Planned features include:

* Multi-tenant organizations and workspace management
* JWT-based authentication with access and refresh tokens
* Role-based access control (Owner, Admin, Agent, Viewer)
* AI customer support agent configuration
* Knowledge base document uploads (PDF, TXT, MD, DOCX)
* Retrieval-Augmented Generation (RAG) using vector search
* Persistent customer conversations
* Human escalation and support agent handoff
* Real-time chat using WebSockets
* API keys for external integrations
* Embeddable JavaScript chat widget
* Analytics and AI usage tracking
* Rate limiting and security hardening
* Dockerized development and production environments
* CI/CD with GitHub Actions

## Architecture

```text
React SPA (TypeScript / Vite)
          │
     HTTPS / REST / WebSocket
          │
Django + Django REST Framework
       + Django Channels
          │
 ┌────────┼────────┐
 │        │        │
PostgreSQL Redis  Celery
(+pgvector)      Workers
                  │
             AI / RAG Pipeline
                  │
      Retriever → Prompt Service
                  │
             LLM Provider
```

## Technology Stack

| Area            | Technologies                                   |
| --------------- | ---------------------------------------------- |
| Backend         | Python, Django, Django REST Framework          |
| Frontend        | React, TypeScript, Vite                        |
| Database        | PostgreSQL, pgvector                           |
| Background Jobs | Celery, Redis                                  |
| Real-time       | Django Channels                                |
| AI/RAG          | Provider-agnostic LLM and embedding interfaces |
| DevOps          | Docker, Docker Compose                         |
| CI/CD           | GitHub Actions                                 |
| Testing         | pytest, Django test framework                  |


## Repository Status

This repository currently contains only the project documentation and initial setup.

Application source code will be added starting from **Phase 1**, following the implementation roadmap.

## Goals

This project aims to demonstrate:

* Clean Django application architecture
* Multi-tenant SaaS design
* Secure REST API development
* Retrieval-Augmented Generation (RAG)
* Agentic AI patterns with controlled tool usage
* Background job processing
* Real-time communication
* Automated testing and tenant isolation
* Containerization and CI/CD
* Production-oriented engineering practices

## Author

**Samyam Giri**


