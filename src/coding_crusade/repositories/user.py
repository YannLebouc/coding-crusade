from coding_crusade.db.connection import get_connection
from coding_crusade.models.user import User
from coding_crusade.dtos.user import UserResponse
from psycopg import class_row


class UserRepository:

    @staticmethod
    def create_user(user: User) -> UserResponse:
        with get_connection(row_factory=class_row(UserResponse)) as conn:
            result = conn.execute(
                """
                    INSERT INTO users(username, password, email)
                    VALUES (%s, %s, %s)
                    RETURNING
                        id
                        ,username
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

        @staticmethod
        def get_user_by_id(id: int) -> UserResponse | None:
            with get_connection(row_factory=class_row(UserResponse)) as conn:
                result = conn.execute(
                    """
                        SELECT 
                            id
                            ,username
                            ,email
                            ,is_admin
                            ,is_active
                            ,created_at
                            ,updated_at
                        FROM users
                        WHERE id = %s
                        ;
                    """,
                    (id),
                ).fetchone()
            return result

            @staticmethod
            def get_user_by_email(email: str) -> UserResponse | None:
                with get_connection(row_factory=class_row(UserResponse)) as conn:
                    result = conn.execute(
                        """
                            SELECT 
                                id
                                ,username
                                ,email
                                ,is_admin
                                ,is_active
                                ,created_at
                                ,updated_at
                            FROM users
                            WHERE email = %s
                            ;
                        """,
                        (email),
                    ).fetchone()
                return result

            @staticmethod
            def get_user_by_username(username: str) -> UserResponse | None:
                with get_connection(row_factory=class_row(UserResponse)) as conn:
                    result = conn.execute(
                        """
                            SELECT 
                                id
                                ,username
                                ,email
                                ,is_admin
                                ,is_active
                                ,created_at
                                ,updated_at
                            FROM users
                            WHERE username = %s
                            ;
                        """,
                        (username),
                    ).fetchone()
                return result
