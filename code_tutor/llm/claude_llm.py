import anthropic
from langchain.chat_models import ChatAnthropic
from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Any, List, Optional
from code_tutor.config import ANTHROPIC_API_KEY


class ClaudeLLM(ChatAnthropic):
    model_name = "claude-3-sonnet-20240229"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    @property
    def _llm_type(self) -> str:
        return "claude"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        message = self.client.messages.create(
            model=self.model_name,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text