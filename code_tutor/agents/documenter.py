from crewai import Agent
from code_tutor.llm.claude_llm import ClaudeLLM
from code_tutor.llm.openai_llm import OpenAILLM
from code_tutor.llm.local_llm import llama31

class Documenter(Agent):
    def __init__(self):
        super().__init__(
            role='Code Documenter',
            goal='Create clear and comprehensive documentation for the code',
            backstory='You are a technical writer with a deep understanding of programming concepts and best practices in documentation.',
            verbose=True,
            allow_delegation=False,
            llm=llama31
        )