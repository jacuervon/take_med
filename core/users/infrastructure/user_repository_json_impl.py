import json
from core.users.domain.user import User
from core.users.domain.user_repository import UserRepository


class UserRepositoryJsonImpl(UserRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data['users'] if 'users' in data else []
        except FileNotFoundError:
            with open(self.file_path, 'w') as file:
                json.dump({'users': []}, file, indent=4)
            return []

    def _save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump({'users': self.users}, file, indent=4)

    def _generate_id(self):
        id = self.users[len(self.users) - 1]['id'] if len(self.users) > 0 else 0
        return id + 1

    def create(self, user: User) -> int:
        new_user = {
            'id': self._generate_id(),
            'name': user.name,
            'last_name': user.last_name,
            'birthday': user.birthday,
        }
        self.users.append(new_user)
        self._save_data()
        return new_user['id']

    def delete(self, user_to_remove: User) -> None:
        for user in self.users:
            if int(user['id']) == user_to_remove.id:

                self.users.remove(user)
                self._save_data()
                return
        raise Exception('User not found')

    def get_all(self) -> list[User]:
        users = []
        for user in self.users:
            users.append(
                User(
                    id=user['id'],
                    name=user['name'],
                    last_name=user['last_name'],
                    birthday=user['birthday'],
                )
            )
        return users

    def get_by_id(self, user_id: int) -> User:
        for user in self.users:
            if int(user['id']) == user_id:
                return User(
                    id=user['id'],
                    name=user['name'],
                    last_name=user['last_name'],
                    birthday=user['birthday'],
                )
        raise Exception('User not found')
