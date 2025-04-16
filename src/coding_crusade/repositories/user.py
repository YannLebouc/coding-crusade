from coding_crusade.db.connection import get_connection
from coding_crusade.models.user import User
from psycopg import DatabaseError, class_row
import logging

logger = logging.getLogger(__name__)


class UserRepository:

    @staticmethod
    def create_user(user: User) -> User:
        try:
            with get_connection(row_factory=class_row(User)) as conn:
                result = conn.execute(
                    """
                        INSERT INTO users(username, password, email)
                        VALUES (%s, %s, %s)
                        RETURNING
                            id
                            ,username
                            ,password
                            ,email
                            ,is_admin
                            ,is_active
                            ,created_at
                            ,updated_at
                        ;
                    """,
                    (user.username, user.password, user.email),
                ).fetchone()
            return result
        except DatabaseError as e:
            logger.error("Erreur lors de la création de l'utilisateur : %s", e)
            raise
