import psycopg
from config import settings

database_url = settings.DATABASE_URL
database_connection = psycopg.connect(database_url)
