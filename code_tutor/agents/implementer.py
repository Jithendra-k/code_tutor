from crewai import Agent
from code_tutor.llm.claude_llm import ClaudeLLM
from code_tutor.llm.openai_llm import OpenAILLM
from code_tutor.llm.local_llm import llama31

class Implementer(Agent):
    def __init__(self):
        super().__init__(
            role='Code Implementer',
            goal='Implement code based on plans and requirements',
            backstory='You are a skilled programmer proficient in multiple programming languages and best coding practices.',
            verbose=True,
            allow_delegation=False,
            llm=llama31
        )