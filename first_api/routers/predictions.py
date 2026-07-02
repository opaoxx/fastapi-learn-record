from fastapi import APIRouter

from ..schemas import PredictionRequest, PredictionResponse


router = APIRouter(tags=["predictions"])


@router.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    positive_words = {"good", "great", "love", "pleasant", "nice", "happy"}
    tokens = {word.strip(".,!?;:").lower() for word in payload.text.split()}
    is_positive = bool(tokens & positive_words)
    careful_bonus = 0.04 if payload.mode == "careful" else 0.0

    score = (0.91 if is_positive else 0.55) + careful_bonus

    return PredictionResponse(
        label="positive" if is_positive else "neutral",
        score=round(score, 2),
        source="rule-based-demo",
        text_length=len(payload.text),
    )
