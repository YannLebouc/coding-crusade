from dataclasses import dataclass, field
from datetime import datetime, UTC
from werkzeug import generate_password_hash, check_password_hash

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from models.projects import Project


@dataclass
class User:
    id: int
    username: str
    password: str
    email: str
    is_admin: bool = field(default=False)
    is_active: bool = field(default=True)
    created_at: datetime = field(default=datetime.now(UTC))
    updated_at: datetime = field(default=datetime.now(UTC))
    # projects: list(Project) = []

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
