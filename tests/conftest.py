"""Test configuration for Customer Insights Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "customer-insights-agent", "category": "Business Intelligence"}
