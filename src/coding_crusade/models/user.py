from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

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
