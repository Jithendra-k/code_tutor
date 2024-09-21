import pytest
from unittest.mock import patch, MagicMock
from main import code_tutor

@pytest.fixture
def mock_crew():
    with patch('coding_mentor.main.Crew') as mock:
        yield mock

def test_code_mentor(mock_crew):
    mock_crew_instance = MagicMock()
    mock_crew_instance.kickoff.return_value = "Test result"
    mock_crew.return_value = mock_crew_instance

    result = code_tutor("Test project description")

    assert result == "Test result"
    mock_crew.assert_called_once()
    mock_crew_instance.kickoff.assert_called_once_with(
        inputs={"project_description": "Test project description"}
    )