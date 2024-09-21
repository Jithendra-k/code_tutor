from crewai import Agent
from langchain.llms import Ollama
from code_tutor.llm.claude_llm import ClaudeLLM
from code_tutor.llm.openai_llm import OpenAILLM
from code_tutor.llm.local_llm import llama31


class Planner(Agent):
    def __init__(self):
        super().__init__(
            role='Code Planner',
            goal='Create high-level plans and architectures for coding projects',
            backstory='You are an experienced software architect with a knack for designing efficient and scalable systems.',
            verbose=True,
            allow_delegation=False,
            llm=llama31
        )