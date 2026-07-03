from dataclasses import dataclass
from typing import Literal


PredictionLabel = Literal["positive", "neutral"]


@dataclass(frozen=True)
class PredictionResult:
    label: PredictionLabel
    score: float
    source: str


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

    def predict_sentiment(self, text: str, mode: str) -> PredictionResult:
        self._raise_if_failure_requested(text)
        tokens = {word.strip(".,!?;:").lower() for word in text.split()}
        is_positive = bool(tokens & self.positive_words)
        careful_bonus = 0.04 if mode == "careful" else 0.0
        score = (0.91 if is_positive else 0.55) + careful_bonus

        return PredictionResult(
            label="positive" if is_positive else "neutral",
            score=round(score, 2),
            source="demo-ai-client",
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


def get_ai_client() -> DemoAIClient:
    return DemoAIClient()
