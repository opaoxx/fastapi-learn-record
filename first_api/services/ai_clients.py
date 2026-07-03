from dataclasses import dataclass
from typing import Literal, Protocol

from ..settings import get_settings


PredictionLabel = Literal["positive", "neutral"]
AIProvider = Literal["demo"]


@dataclass(frozen=True)
class PredictionResult:
    label: PredictionLabel
    score: float
    source: str


@dataclass(frozen=True)
class AIClientConfig:
    provider: AIProvider = "demo"
    timeout_seconds: float = 10.0
    max_attempts: int = 1


class AIClient(Protocol):
    def predict_sentiment(self, text: str, mode: str) -> PredictionResult:
        ...

    def summarize(self, text: str) -> str:
        ...


class AIClientError(Exception):
    def __init__(
        self,
        message: str = "The AI service is temporarily unavailable.",
        error_code: str = "ai_client_unavailable",
    ) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code


class DemoAIClient:
    positive_words = {"good", "great", "love", "pleasant", "nice", "happy"}
    failure_marker = "simulate-ai-failure"

    def __init__(self, config: AIClientConfig | None = None) -> None:
        self.config = config or AIClientConfig()

    def predict_sentiment(self, text: str, mode: str) -> PredictionResult:
        self._raise_if_failure_requested(text)
        tokens = {word.strip(".,!?;:").lower() for word in text.split()}
        is_positive = bool(tokens & self.positive_words)
        careful_bonus = 0.04 if mode == "careful" else 0.0
        score = (0.91 if is_positive else 0.55) + careful_bonus

        return PredictionResult(
            label="positive" if is_positive else "neutral",
            score=round(score, 2),
            source=f"{self.config.provider}-ai-client",
        )

    def summarize(self, text: str) -> str:
        self._raise_if_failure_requested(text)
        words = text.split()
        if len(words) <= 12:
            return text
        return " ".join(words[:12]) + " ..."

    def _raise_if_failure_requested(self, text: str) -> None:
        if self.failure_marker in text.lower():
            raise AIClientError(
                message="The demo AI client was asked to simulate a failure.",
                error_code="demo_ai_failure",
            )


def build_ai_client_config() -> AIClientConfig:
    settings = get_settings()
    return AIClientConfig(
        provider=settings.ai_provider,
        timeout_seconds=settings.ai_timeout_seconds,
        max_attempts=settings.ai_max_attempts,
    )


def get_ai_client() -> AIClient:
    return DemoAIClient(config=build_ai_client_config())
