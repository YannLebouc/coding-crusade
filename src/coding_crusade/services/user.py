from coding_crusade.repositories.user import UserRepository as ur
from coding_crusade.models.user import User
from coding_crusade.dtos.user import UserCreation
from werkzeug import generate_password_hash
from coding_crusade.exceptions import UsernameAlreadyUsedError, EmailAlreadyUsedError


class UserService:

    @staticmethod
    def register_user(user: UserCreation) -> User:
        new_user = User(
            username=user.username,
            password=generate_password_hash(user.password),
            email=user.email,
        )

        if ur.get_user_by_email(new_user.email):
            raise EmailAlreadyUsedError(
                f"L'adresse email {new_user.email} est déjà utilisée, la création de l'inscription a échouée"
            )

        if ur.get_user_by_username(new_user.username):
            raise UsernameAlreadyUsedError(
                f"Le nom d'utilisateur {new_user.username} est déjà utilisé, la création de l'inscription a échouée"
            )

        return ur.create_user(new_user)
