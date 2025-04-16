from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class UserResponse:
    id: int
    username: str
    email: str
    is_admin: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime
