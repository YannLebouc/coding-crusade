import psycopg
from typing import Any
from coding_crusade.config import settings


def get_connection(**kwargs: Any) -> psycopg.Connection:
    return psycopg.connect(settings.DATABASE_URL, **kwargs)
