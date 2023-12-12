from core.users.domain.user import User
from core.users.application.user_create_use_case import UserCreateUseCase
from core.users.application.user_delete_use_case import UserDeleteUseCase
from core.users.application.user_get_all_use_case import UserGetAllUseCase
from core.users.application.user_get_by_id_use_case import UserGetByIdUseCase
from core.users.infrastructure.user_repository_json_impl import UserRepositoryJsonImpl


def test_user_model():
    user = User(
        name="John",
        last_name="Doe",
        birthday="1990-01-01",
        id=1
    )
    assert user.id == 1
    assert user.name == "John"
    assert user.last_name == "Doe"
    assert user.birthday == "1990-01-01"


def setup():
    test_file = './test/data/users.json'
    user_repository = UserRepositoryJsonImpl(test_file)
    user_create_use_case = UserCreateUseCase(user_repository)
    user_delete_use_case = UserDeleteUseCase(user_repository)
    user_get_all_use_case = UserGetAllUseCase(user_repository)
    user_get_by_id_use_case = UserGetByIdUseCase(user_repository)

    user_1 = User(
        name="Julian",
        last_name="Cuervo",
        birthday="2000-01-21",
        id=1
    )

    user_2 = User(
        name="John",
        last_name="Doe",
        birthday="1990-01-01",
        id=2
    )

    return user_create_use_case, user_delete_use_case, user_get_all_use_case, user_get_by_id_use_case, user_1, user_2


def test_create():
    user_create_use_case, _, _, _, user_1, user_2 = setup()
    user_id = user_create_use_case.execute(user_1)
    assert user_id == 1
    user_id = user_create_use_case.execute(user_2)
    assert user_id == 2


def test_get_by_id():
    _, _, _, user_get_by_id_use_case, _, user_2 = setup()

    user = user_get_by_id_use_case.execute(user_2.id)
    assert user.id == 2
    assert user.name == "John"
    assert user.last_name == "Doe"
    assert user.birthday == "1990-01-01"


def test_get_all():
    _, _, user_get_all_use_case, _, _, _ = setup()
    users = user_get_all_use_case.execute()
    assert len(users) == 2


def test_delete():
    _, user_delete_use_case, user_get_all_use_case, _, user_1, user_2 = setup()
    user_delete_use_case.execute(user_2)
    users = user_get_all_use_case.execute()
    assert len(users) == 1
    user_delete_use_case.execute(user_1)
    users = user_get_all_use_case.execute()
    assert len(users) == 0
