'''from fastapi import APIRouter, HTTPException, Request

from config import config
from services import fetch_json
from schema import (
    AIDeploymentRequest,
    HealthItem,
    Driver,
)

router = APIRouter()


@router.post("/completions")
async def completions(
    request_body: AIDeploymentRequest,
    request: Request,
):
    response = request.app.state.completion_response

    return {
        "api_version": "v2",
        "data": response,
    }


@router.get(
    "/health",
    response_model=list[HealthItem]
)
async def health():
    try:
        data = await fetch_json(
            config["request_paths"]["health_requests"]
        )

        return data

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Health endpoint failed: {str(e)}",
        )


@router.get("/models")
async def models():
    try:
        data = await fetch_json(
            config["request_paths"]["models_requests"]
        )

        return {
            "api_version": "v2",
            "count": len(data),
            "drivers": data,
        }

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Models endpoint failed: {str(e)}",
        )'''