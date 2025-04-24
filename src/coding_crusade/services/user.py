from coding_crusade.repositories.user import UserRepository as ur
from coding_crusade.models.user import User
from coding_crusade.dtos.user import UserCreation
from werkzeug import generate_password_hash


class UserService:

    @staticmethod
    def register_user(user: UserCreation) -> User:

        if ur.get_user_by_email(user.email):
            raise EmailAlreadyUsedError(user.email)

        if ur.get_user_by_username(user.username):
            raise UsernameAlreadyUsedError(user.username)

        new_user = User(
            username=user.username,
            password=generate_password_hash(user.password),
            email=user.email,
        )

        return ur.create_user(new_user)


class UserError(Exception): ...


class EmailAlreadyUsedError(UserError):
    def __init__(self, email: str):
        super().__init__(f'Email adress "{email}" is already in use')


class UsernameAlreadyUsedError(UserError):
    def __init__(self, username: str):
        super().__init__(f'Username "{username}" is already in use')
