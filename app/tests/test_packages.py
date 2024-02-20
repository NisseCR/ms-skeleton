from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_packages():
    response = client.get(url="/packages/", headers={"X-Token": "secret"})
    assert response.status_code == 200
    assert response.json() == {
          "data": {
            "fastapi": {
              "name": "FastAPI",
              "version": "1.0.0",
              "description": "foo"
            },
            "pydantic": {
              "name": "Pydantic",
              "version": "1.0.0",
              "description": "foo"
            }
          }
        }


