from dataclasses import dataclass, field

from mygamecollection.domain.entities.game import Game


@dataclass
class User:
    login: str
    first_name: str
    last_name: str
    id: int | None = None
    games: list[Game] = field(default_factory=list)

    def __post_init__(self):
        if not self.login.strip():
            raise ValueError("Login cannot be empty")
        if not self.first_name.strip():
            raise ValueError("First name cannot be empty")
        if not self.last_name.strip():
            raise ValueError("Last name cannot be empty")

    @classmethod
    def create(
            cls,
            login: str,
            first_name: str,
            last_name: str
    ):
        if not login.strip():
            raise ValueError("Login cannot be empty")
        if not first_name.strip():
            raise ValueError("First name cannot be empty")
        if not last_name.strip():
            raise ValueError("Last name cannot be empty")

        return cls(
            login = login,
            first_name = first_name,
            last_name = last_name
        )

    def update(
            self,
            login: str,
            first_name: str,
            last_name: str,
    ):
        if not login.strip():
            raise ValueError("Login cannot be empty")
        if not first_name.strip():
            raise ValueError("First name cannot be empty")
        if not last_name.strip():
            raise ValueError("Last name cannot be empty")

        self.login = login
        self.first_name = first_name
        self.last_name = last_name