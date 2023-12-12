import random
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

def test_uses_cases():
    random_number = random.randint(1, 1000);
    test_file = './test/data/users'+str(random_number)+'.json'  
    user_repository = UserRepositoryJsonImpl(test_file)
    user_create_use_case = UserCreateUseCase(user_repository)
    user_delete_use_case = UserDeleteUseCase(user_repository)
    user_get_all_use_case = UserGetAllUseCase(user_repository)
    user_get_by_id_use_case = UserGetByIdUseCase(user_repository)

    user_1 = User(
        name="John",
        last_name="Doe",
        birthday="1990-01-01",
        id=1
    )

    user_2 = User(
        name="John",
        last_name="Doe",
        birthday="1990-01-01",
        id=1
    )

    ## Test create
    user_id = user_create_use_case.execute(user_1)
    assert user_id == 1
    user_id = user_create_use_case.execute(user_2)
    assert user_id == 2

    ## Test get by id
    user = user_get_by_id_use_case.execute(user_id)
    assert user.id == 2
    assert user.name == "John"
    assert user.last_name == "Doe"
    assert user.birthday == "1990-01-01"

    ## Test get all
    users = user_get_all_use_case.execute()
    assert len(users) == 2

    ## Test delete
    user_delete_use_case.execute(user)
    users = user_get_all_use_case.execute()
    assert len(users) == 1



