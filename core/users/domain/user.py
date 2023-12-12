class User:
    def __init__(self, name: str, last_name: str, birthday: str, id: int = None) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
