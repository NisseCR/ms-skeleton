from pydantic import BaseModel


class Package(BaseModel):
    name: str
    version: str
    description: str | None = None


class Packages(BaseModel):
    data: dict[str, Package]
