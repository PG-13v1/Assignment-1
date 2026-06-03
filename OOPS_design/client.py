from abc import ABC, abstractmethod
import requests
from typing import Any


class CompletionClient(ABC):
    """Abstract completion client."""

    @abstractmethod
    def summarize(
        self,
        prompt: str,
        customer_id: str,
    ) -> str | None:
        """
        Generate a summary.

        Returns None on failure.
        """
        ...


class RequestsCompletionClient(
    CompletionClient
):
    """Requests-based implementation."""

    def __init__(
        self,
        api_url: str,
        api_key: str,
        model: str,
        system_prompt: str,
    ) -> None:

        self.api_url = api_url
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt

        self.total_tokens: int = 0

    def summarize(
        self,
        prompt: str,
        customer_id: str,
    ) -> str | None:

        headers = {
            "Authorization":
                f"Bearer {self.api_key}",
            "Content-Type":
                "application/json",
        }

        body: dict[str, Any] = {
          "model": self.model,
          "messages": [
          {
            "role": "system",
            "content": self.system_prompt,
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],}

        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=body,
                timeout=10,
            )

            if response.status_code != 200:
                return None

            data = response.json()

            self.total_tokens += (
                data.get(
                    "usage",
                    {},
                ).get(
                    "total_tokens",
                    0,
                )
            )

            content = (data["choices"][0]["message"]["content"])

            if not isinstance(content, str):
               return None

            return content

        except requests.RequestException:
            return None