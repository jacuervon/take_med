from core.users.domain.user import User
from core.users.domain.user_repository import UserRepository

class UserDeleteUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user: User) -> None:
        self.user_repository.delete(user)