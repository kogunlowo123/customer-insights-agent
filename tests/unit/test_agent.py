"""Customer Insights Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_cohort():
    """Test Perform cohort analysis on retention, revenue, or engagement."""
    tools = AgentTools()
    result = await tools.analyze_cohort(cohort_type="test", metric="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_segment_customers():
    """Test Segment customers by behavior, value, or engagement patterns."""
    tools = AgentTools()
    result = await tools.segment_customers(features="test", method="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_predict_churn():
    """Test Predict churn probability for individual customers or segments."""
    tools = AgentTools()
    result = await tools.predict_churn(customer_ids="test", segment="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_calculate_ltv():
    """Test Calculate customer lifetime value by segment and cohort."""
    tools = AgentTools()
    result = await tools.calculate_ltv(method="test", segments="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.customer_insights_agent_agent import CustomerInsightsAgentAgent
    agent = CustomerInsightsAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
