from core.users.domain.user import User


class UserRepository:
    def create(self, user: User) -> int:
        pass

    def delete(self, user: User) -> None:
        pass

    def get_all(self) -> list[User]:
        pass

    def get_by_id(self, user_id: int) -> User:
        pass
