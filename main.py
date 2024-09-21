from crewai import Crew
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

import warnings
warnings.filterwarnings("ignore")

def code_tutor(project_description):
    crew = Crew(
        agents=[
            Planner(),
            Implementer(),
            Debugger(),
            Documenter(),
            Tester()
        ],
        tasks=[
            create_planning_task(),
            create_implementation_task(),
            create_debugging_task(),
            create_documentation_task(),
            create_testing_task()
        ],
        verbose=True
    )

    result = crew.kickoff(
        inputs={
            "project_description": project_description
        }
    )
    return result


if __name__ == "__main__":
    project_description = """
    Create a Python web application named "GiftShop" using Flask that allows users to create, read, update, and delete (CRUD) tasks.
    The application should use SQLite as its database and include proper error handling and input validation.
    Please implement user authentication and ensure the code follows PEP 8 style guidelines.
    """


    result = code_tutor(project_description)
    print(result)