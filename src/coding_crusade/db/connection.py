import psycopg
from coding_crusade.config import settings


def get_connection():
    return psycopg.connect(settings.DATABASE_URL)
