from core.users.domain.user import User
from core.users.domain.user_repository import UserRepository

class UserCreateUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user: User) -> int:
        user_id = self.user_repository.create(user)
        return user_id
        