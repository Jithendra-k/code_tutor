import pytest
from unittest.mock import patch, MagicMock
from code_tutor.llm.claude_llm import ClaudeLLM

@pytest.fixture
def mock_anthropic():
    with patch('anthropic.Anthropic') as mock:
        yield mock

def test_claude_llm_initialization(mock_anthropic):
    llm = ClaudeLLM()
    assert llm.model_name == "claude-3-sonnet-20240229"
    assert llm._llm_type == "claude"

def test_claude_llm_call(mock_anthropic):
    mock_client = MagicMock()
    mock_client.messages.create.return_value = MagicMock(content=[MagicMock(text="Test response")])
    mock_anthropic.return_value = mock_client

    llm = ClaudeLLM()
    response = llm._call("Test prompt")

    assert response == "Test response"
    mock_client.messages.create.assert_called_once_with(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": "Test prompt"}]
    )