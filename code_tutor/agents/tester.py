from crewai import Agent
from code_tutor.llm.claude_llm import ClaudeLLM
from code_tutor.llm.openai_llm import OpenAILLM
from code_tutor.llm.local_llm import llama31


class Tester(Agent):
    def __init__(self):
        super().__init__(
            role='Code Tester',
            goal='Design and implement tests to ensure code quality and functionality',
            backstory='You are a quality assurance expert with a strong background in various testing methodologies and frameworks.',
            verbose=True,
            allow_delegation=False,
            llm=llama31
        )