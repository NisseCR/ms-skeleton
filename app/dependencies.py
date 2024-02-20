from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    """Placeholder authentication."""
    if x_token != "secret":
        raise HTTPException(status_code=400, detail="X-Token header invalid")