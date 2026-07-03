from dataclasses import dataclass
from typing import Literal


PredictionLabel = Literal["positive", "neutral"]


@dataclass(frozen=True)
class PredictionResult:
    label: PredictionLabel
    score: float
    source: str


class DemoAIClient:
    positive_words = {"good", "great", "love", "pleasant", "nice", "happy"}

    def predict_sentiment(self, text: str, mode: str) -> PredictionResult:
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
        words = text.split()
        if len(words) <= 12:
            return text
        return " ".join(words[:12]) + " ..."


def get_ai_client() -> DemoAIClient:
    return DemoAIClient()
