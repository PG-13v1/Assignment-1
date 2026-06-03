from datetime import datetime, timedelta, UTC

import jwt

from fastapi import (
    Depends,
    HTTPException,
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

security = HTTPBearer()

RATE_LIMIT = 5

token_requests = {}


def create_access_token(username: str):
    expire = (
        datetime.now(UTC)
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": username,
        "exp": expire,
    }
    print("Expire:", expire)

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        token_requests[token] = (
            token_requests.get(token, 0) + 1
        )
          
        print("Decoded payload:", payload)

        if token_requests[token] > RATE_LIMIT:
            raise HTTPException(
                status_code=429,
                detail="rate limit exceeded",
            )
        return payload["sub"]

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="token expired",
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="invalid token",
        )

