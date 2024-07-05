from typing import AsyncGenerator,Generator

import pytest_
from fastapi.testclient import TestClient
from httpx import AsyncClient

from main import app
from routers.post import comment_table, post_table

def client() -> Generator:
    yield