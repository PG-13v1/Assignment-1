from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import config
from services import load_json_file
from schema import AIDeploymentRequest

'''from api.v1.routes import router as v1_router'''
from api.v2.routes import router as v2_router

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import (
    Request,
    HTTPException,
)


def problem_response(
    status: int,
    title: str,
    detail: str,
    instance: str,
    type_: str,
):
    return JSONResponse(
        status_code=status,
        content={
            "type": type_,
            "title": title,
            "status": status,
            "detail": detail,
            "instance": instance,
        },
        media_type="application/problem+json",
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    raw_data_response = load_json_file(
        config["outbounds"]["completion_posts"]
    )

    app.state.completion_response = (
        AIDeploymentRequest.model_validate(
            raw_data_response
        )
    )

    yield


app = FastAPI(
    title="Mock OpenAI API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(
    v2_router,
    prefix="/v1",
    tags=["v1"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "type": "https://example.com/problems/validation-error",
            "title": "Validation Error",
            "status": 422,
            "detail": "Request body validation failed",
            "instance": request.url.path,
            "errors": exc.errors(),
        },
        media_type="application/problem+json",
    )

@app.exception_handler(
    HTTPException
)
async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "type":
                f"https://example.com/problems/{exc.status_code}",
            "title": "HTTP Error",
            "status": exc.status_code,
            "detail": str(exc.detail),
            "instance": request.url.path,
        },
        media_type="application/problem+json",
    )


@app.exception_handler(Exception)
async def internal_error_handler(
    request: Request,
    exc: Exception
):
    return problem_response(
        status=500,
        title="Internal Server Error",
        detail="An unexpected error occurred",
        instance=request.url.path,
        type_="https://example.com/problems/internal-server-error",
    )