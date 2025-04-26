import re
from email_validator import validate_email, EmailNotValidError
from coding_crusade.validators.base import ValidatorError

PASSWORD_RULES = """
- Be at least 8 characters long
- Contain :
     - One capital letter
     - One small letter
     - One special character
     - One number
"""

USERNAME_RULES = """
- Be between 3 and 20 alphanumeric characters long
- Not contain any other special character than the underscore (_)
"""


class UserValidator:
    def validate_email(email: str) -> str:
        try:
            email = validate_email(email)
        except EmailNotValidError as e:
            raise InvalidEmailError(email, str(e)) from e

        return email.normalized

    def validate_username(username: str) -> str:
        # Pattern based on USERNAME_RULES const
        pattern = r"^[a-zA-Z0-9_]{3,20}$"
        if not re.match(pattern, username):
            raise InvalidUsernameError(username)

        return username.lower().strip()

    def validate_password(password: str) -> str:
        # Pattern based on PASSWORD_RULES const
        pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if not re.match(pattern, password):
            raise InvalidPasswordError(password)

        return password


class InvalidEmailError(ValidatorError):
    # Email validation always inherits third-party validate_email() Exception message
    def __init__(self, email: str, inherited_message: str):
        super().__init__(
            f'The email adress "{email}" is not valid : {inherited_message}'
        )


class InvalidUsernameError(ValidatorError):
    def __init__(self, username: str):
        super().__init__(f'Invalid username "{username}". It must :\n{USERNAME_RULES}')


class InvalidPasswordError(ValidatorError):
    def __init__(self, password: str):
        super().__init__(f'Invalid password "{password}". It must :\n{PASSWORD_RULES}')
