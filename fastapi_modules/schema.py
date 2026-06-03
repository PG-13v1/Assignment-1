
from pydantic import BaseModel, Field
from typing import Dict, Any

class LoginRequest(BaseModel):
    username: str
    password: str


class AIDeploymentRequest(BaseModel):
    request_id: str = Field(
        pattern=r"^req_.*",
        min_length=5
    )

    task: str = Field(
        min_length=5,
        max_length=500
    )

    models: Dict[str, Any]

    pipeline: Dict[str, bool]

    deployment: Dict[str, Any]


class HealthItem(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=200
    )

    bite: str = Field(
        min_length=1,
        max_length=1000
    )

    url: str = Field(
        min_length=1,
        pattern=r"^/.*"
    )

class Driver(BaseModel):
    driver_number: int = Field(
        ge=1,
        le=99,
        description="F1 driver number"
    )

    broadcast_name: str = Field(
        min_length=1,
        max_length=50
    )

    team_name: str = Field(
        min_length=1,
        max_length=50
    )

    team_colour: str = Field(
        pattern=r"^[A-Fa-f0-9]{6}$",
        description="6-digit hex color without #"
    )

    full_name: str = Field(
        min_length=3,
        max_length=100
    )

    country_code: str = Field(
        pattern=r"^[A-Z]{3}$",
        description="ISO 3166-1 alpha-3 country code"
    )
