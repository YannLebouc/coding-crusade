import re
from email_validator import validate_email, EmailNotValidError
from coding_crusade.validators.base import ValidatorError


class UserValidator:
    def validate_email(email: str) -> str:
        try:
            email = validate_email(email)
        except EmailNotValidError as e:
            raise InvalidEmailError(email, str(e)) from e

        return email.normalized

    def validate_username(username: str) -> str:
        # statement to be determined according to validation rules
        if not statement:
            raise InvalidUsernameError(username)

        return username

    def validate_password(password: str) -> str:
        # Regex to be written according to validation rules
        if not re.match("", password):
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
        super().__init__(
            f"""Invalid username \"{username}\". It must : 
                - Be between 3 and 20 alphanumeric characters long
                - Not contain any other special character than the underscore (_)
             """
        )


class InvalidPasswordError(ValidatorError):
    def __init__(self, password: str):
        super().__init__(
            f"""Invalid password \"{password}\". It must :
                - Be at least 8 characters long
                - Contain :
                    - one capital letter
                    - one small letter
                    - one special character
            """
        )
