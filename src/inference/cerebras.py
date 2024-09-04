from tenacity import retry,stop_after_attempt,retry_if_exception_type
from requests import post,RequestException,HTTPError
from src.message import AIMessage,BaseMessage
from src.inference import BaseInference
from typing import Generator
from json import loads

class ChatCerebras(BaseInference):
    @retry(stop=stop_after_attempt(3),retry=retry_if_exception_type(RequestException))
    def invoke(self, messages: list[BaseMessage],json:bool=False)->AIMessage:
        self.headers.update({'Authorization': f'Bearer {self.api_key}'})
        headers=self.headers
        temperature=self.temperature
        url=self.base_url or "https://api.cerebras.ai/v1/chat/completions"
        messages=[message.to_dict() for message in messages]
        payload={
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "stream":False,
        }