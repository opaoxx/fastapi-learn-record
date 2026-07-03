from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ..schemas import ErrorResponse, PredictionRequest, PredictionResponse
from ..services.ai_clients import AIClient, AIClientError, get_ai_client


router = APIRouter(tags=["predictions"])


@router.post(
    "/predict",
    response_model=PredictionResponse,
    responses={status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse}},
)
def predict(
    payload: PredictionRequest,
    ai_client: Annotated[AIClient, Depends(get_ai_client)],
) -> PredictionResponse:
    try:
        prediction = ai_client.predict_sentiment(payload.text, payload.mode)
    except AIClientError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error_code": exc.error_code,
                "message": exc.message,
            },
        ) from exc

    return PredictionResponse(
        label=prediction.label,
        score=prediction.score,
        source=prediction.source,
        text_length=len(payload.text),
    )
