import pytest
from code_tutor.tasks.task_definitions import (
    create_planning_task,
    create_implementation_task,
    create_debugging_task,
    create_documentation_task,
    create_testing_task
)
from code_tutor.agents.planner import Planner
from code_tutor.agents.implementer import Implementer
from code_tutor.agents.debugger import Debugger
from code_tutor.agents.documenter import Documenter
from code_tutor.agents.tester import Tester

def test_planning_task():
    task = create_planning_task()
    assert task.description == 'Create a high-level plan for the coding project'
    assert isinstance(task.agent, Planner)

def test_implementation_task():
    task = create_implementation_task()
    assert task.description == 'Implement the code based on the provided plan'
    assert isinstance(task.agent, Implementer)

def test_debugging_task():
    task = create_debugging_task()
    assert task.description == 'Review the implemented code, identify any issues, and suggest improvements'
    assert isinstance(task.agent, Debugger)

def test_documentation_task():
    task = create_documentation_task()
    assert task.description == 'Create comprehensive documentation for the implemented code'
    assert isinstance(task.agent, Documenter)

def test_testing_task():
    task = create_testing_task()
    assert task.description == 'Design and implement tests for the code'
    assert isinstance(task.agent, Tester)
