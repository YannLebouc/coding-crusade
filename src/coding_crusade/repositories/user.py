from coding_crusade.db.connection import get_connection
from coding_crusade.models.user import User
from psycopg import DatabaseError, class_row


class UserRepository:

    def create_user(user: User) -> User:
        try:
            with get_connection(row_factory=class_row(User)) as conn:
                result = conn.execute(
                    """
                        INSERT INTO users(username, password, email)
                        VALUES (%s, %s, %s);
                    """,
                    (user.username, user.password, user.email),
                ).fetchone()
            return result
        except DatabaseError as e:
            print("Erreur lors de la création de l'utilisateur " + e)
