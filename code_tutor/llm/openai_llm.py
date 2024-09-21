import openai
import time
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Any, List, Optional
from code_tutor.config import OPENAI_API_KEY
from code_tutor.config import OPENAI_MODEL_NAME
from litellm.exceptions import RateLimitError


class OpenAILLM(ChatOpenAI):
    model_name = OPENAI_MODEL_NAME

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_key = OPENAI_API_KEY

    @property
    def _llm_type(self) -> str:
        return "openai"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1000,
                    stop=stop,
                    **kwargs
                )
                return response['choices'][0]['message']['content']
            except RateLimitError:
                print("Rate limit exceeded. Waiting before retrying...")
                time.sleep(10)  # Wait for 10 seconds before retrying
