from crewai import Agent
from code_tutor.llm.claude_llm import ClaudeLLM
from code_tutor.llm.openai_llm import OpenAILLM
from code_tutor.llm.local_llm import llama31


class Debugger(Agent):
    def __init__(self):
        super().__init__(
            role='Code Debugger',
            goal='Identify and fix issues in code',
            backstory='You are an expert at troubleshooting and optimizing code, with a keen eye for detecting bugs and inefficiencies.',
            verbose=True,
            allow_delegation=False,
            llm=llama31
        )