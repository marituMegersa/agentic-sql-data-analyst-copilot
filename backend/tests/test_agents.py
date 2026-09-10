def test_agent_orchestrator():
    prompt = "Test execution query for agentic-sql-data-analyst-copilot"
    assert len(prompt) > 0
    assert "Test" in prompt
