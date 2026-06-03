from fastapi import (
    APIRouter,
    HTTPException,
    Request,
    Depends,
)

from config import config

from services import fetch_json

from schema import (
    AIDeploymentRequest,
    HealthItem,
    Driver,
    LoginRequest,
)

from auth import (
    create_access_token,
    verify_token,
)

router = APIRouter()


@router.post("/auth/token")
async def auth_token(
    credentials: LoginRequest,
):
    if (
        credentials.username != "admin"
        or credentials.password != "password"
    ):
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )

    token = create_access_token(
        credentials.username
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.post("/completions")
async def completions(
    request_body: AIDeploymentRequest,
    request: Request,
    username: str = Depends(
        verify_token
    ),
):
    response = (
        request.app.state.completion_response
    )

    return {
        "api_version": "v1",
        "user": username,
        "data": response,
    }


@router.get(
    "/health",
    response_model=list[HealthItem],
)
async def health():
    try:
        data = await fetch_json(
            config["request_paths"][
                "health_requests"
            ]
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
            config["request_paths"][
                "models_requests"
            ]
        )

        return {
            "api_version": "v1",
            "count": len(data),
            "drivers": data,
        }

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Models endpoint failed: {str(e)}",
        )