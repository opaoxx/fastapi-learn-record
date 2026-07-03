from typing import Annotated

from fastapi import APIRouter, Depends

from ..schemas import PredictionRequest, PredictionResponse
from ..services.ai_clients import DemoAIClient, get_ai_client


router = APIRouter(tags=["predictions"])


@router.post("/predict", response_model=PredictionResponse)
def predict(
    payload: PredictionRequest,
    ai_client: Annotated[DemoAIClient, Depends(get_ai_client)],
) -> PredictionResponse:
    prediction = ai_client.predict_sentiment(payload.text, payload.mode)
    return PredictionResponse(
        label=prediction.label,
        score=prediction.score,
        source=prediction.source,
        text_length=len(payload.text),
    )
