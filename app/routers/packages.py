from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header
from ..models.package import Package, Packages

router = APIRouter(
    prefix="/packages",
    tags=["packages"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

db = {
    "fastapi": Package(name="FastAPI", version="1.0.0", description="foo"),
    "pydantic": Package(name="Pydantic", version="1.0.0", description="foo"),
}


@router.get("/")
def read_packages() -> Packages:
    """
    Return all items from the (dummy) database.
    :return:
    """
    return Packages(data=db)


@router.get("/{item_id}")
def read_package(item_id: str) -> Package:
    """
    Return single item from the (dummy) database.
    :param item_id:
    :return:
    """
    if item_id not in db:
        raise HTTPException(status_code=404)

    return db[item_id]



