import pytest
from code_tutor.agents.planner import Planner
from code_tutor.agents.implementer import Implementer
from code_tutor.agents.debugger import Debugger
from code_tutor.agents.documenter import Documenter
from code_tutor.agents.tester import Tester

def test_planner_initialization():
    planner = Planner()
    assert planner.role == 'Code Planner'
    assert planner.goal == 'Create high-level plans and architectures for coding projects'
    assert planner.verbose == True
    assert planner.allow_delegation == False

def test_implementer_initialization():
    implementer = Implementer()
    assert implementer.role == 'Code Implementer'
    assert implementer.goal == 'Implement code based on plans and requirements'
    assert implementer.verbose == True
    assert implementer.allow_delegation == False

def test_debugger_initialization():
    debugger = Debugger()
    assert debugger.role == 'Code Debugger'
    assert debugger.goal == 'Identify and fix issues in code'
    assert debugger.verbose == True
    assert debugger.allow_delegation == False

def test_documenter_initialization():
    documenter = Documenter()
    assert documenter.role == 'Code Documenter'
    assert documenter.goal == 'Create clear and comprehensive documentation for the code'
    assert documenter.verbose == True
    assert documenter.allow_delegation == False

def test_tester_initialization():
    tester = Tester()
    assert tester.role == 'Code Tester'
    assert tester.goal == 'Design and implement tests to ensure code quality and functionality'
    assert tester.verbose == True
    assert tester.allow_delegation == False