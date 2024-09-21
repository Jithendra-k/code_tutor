from crewai import Task
from code_tutor.agents.planner import Planner
from code_tutor.agents.implementer import Implementer
from code_tutor.agents.debugger import Debugger
from code_tutor.agents.documenter import Documenter
from code_tutor.agents.tester import Tester

def create_planning_task():
    return Task(
        description='Create a high-level plan for the coding project',
        agent=Planner(),
        expected_output='A detailed project plan'
    )

def create_implementation_task():
    return Task(
        description='Implement the code based on the provided plan',
        agent=Implementer(),
        expected_output='The implemented code'
    )

def create_debugging_task():
    return Task(
        description='Review the implemented code, identify any issues, and suggest improvements',
        agent=Debugger(),
        expected_output='List of issues and improvements'
    )

def create_documentation_task():
    return Task(
        description='Create comprehensive documentation for the implemented code',
        agent=Documenter(),
        expected_output='Project documentation'
    )

def create_testing_task():
    return Task(
        description='Design and implement tests for the code',
        agent=Tester(),
        expected_output='Test cases and test results'
    )
