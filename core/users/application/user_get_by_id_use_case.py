from core.users.domain.user import User
from core.users.domain.user_repository import UserRepository


class UserGetByIdUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        return self.user_repository.get_by_id(user_id)