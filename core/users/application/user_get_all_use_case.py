from core.users.domain.user import User
from core.users.domain.user_repository import UserRepository

class UserGetAllUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self) -> list[User]:
        return self.user_repository.get_all()