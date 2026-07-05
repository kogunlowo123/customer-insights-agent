# Customer Insights Agent

[![CI](https://github.com/kogunlowo123/customer-insights-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/customer-insights-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Business Intelligence | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Customer analytics agent that performs cohort analysis, segments customers by behavior and value, predicts churn risk, measures customer lifetime value, and generates persona-driven insights for product and marketing teams.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_cohort` | Perform cohort analysis on retention, revenue, or engagement |
| `segment_customers` | Segment customers by behavior, value, or engagement patterns |
| `predict_churn` | Predict churn probability for individual customers or segments |
| `calculate_ltv` | Calculate customer lifetime value by segment and cohort |
| `generate_persona` | Generate data-driven customer personas from behavioral data |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/customers/cohort` | Analyze cohort |
| `POST` | `/api/v1/customers/segment` | Segment customers |
| `POST` | `/api/v1/customers/churn` | Predict churn |
| `POST` | `/api/v1/customers/ltv` | Calculate LTV |
| `POST` | `/api/v1/customers/persona` | Generate persona |

## Features

- Cohort Analysis
- Behavioral Segmentation
- Churn Prediction
- Ltv Calculation
- Persona Generation

## Integrations

- Segment
- Amplitude
- Mixpanel
- Snowflake
- Salesforce

## Architecture

```
customer-insights-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── customer_insights_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CDP + Data Warehouse + ML Platform**

---

Built as part of the Enterprise AI Agent Platform.
