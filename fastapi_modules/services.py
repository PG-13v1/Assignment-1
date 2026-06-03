import json
from pathlib import Path

import httpx


async def fetch_json(url: str):
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        response.json()
        return response.json()


def load_json_file(path: str):
    file_path = Path(path)

    with file_path.open("r") as f:
        return json.load(f)