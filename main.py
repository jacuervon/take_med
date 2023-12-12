from core.users.domain.user import User
from core.users.application.user_create_use_case import UserCreateUseCase
from core.users.application.user_delete_use_case import UserDeleteUseCase
from core.users.application.user_get_all_use_case import UserGetAllUseCase
from core.users.application.user_get_by_id_use_case import UserGetByIdUseCase
from core.users.infrastructure.user_repository_json_impl import UserRepositoryJsonImpl

user_repository = UserRepositoryJsonImpl('./users.json')
user_create_use_case = UserCreateUseCase(user_repository)
user_delete_use_case = UserDeleteUseCase(user_repository)
user_get_all_use_case = UserGetAllUseCase(user_repository)
user_get_by_id_use_case = UserGetByIdUseCase(user_repository)

if __name__ == "__main__":
    print('Users app')
    print('1. Create user')
    print('2. Delete user')
    print('3. Get all users')
    print('4. Get user by id')
    print('5. Exit')
    while True:
        option = input('Select an option: ')
        if option == '1':
            print('Create user')
            name = input('Name: ')
            last_name = input('Last name: ')
            birthday = input('Birthday: ')
            user = User(name, last_name, birthday)
            user_id = user_create_use_case.execute(user)
            print(f'User created with id {user_id}')
        elif option == '2':
            print('Delete user')
            user_id = input('User id: ')
            user = user_get_by_id_use_case.execute(int(user_id))
            user_delete_use_case.execute(user)
            print(f'User with id {user_id} deleted')
        elif option == '3':
            print('Get all users')
            users = user_get_all_use_case.execute()
            for user in users:
                print(f'{user.id} - {user.name} {user.last_name} - {user.birthday}')
        elif option == '4':
            print('Get user by id')
            user_id = input('User id: ')
            user = user_get_by_id_use_case.execute(int(user_id))
            print(f'{user.id} - {user.name} {user.last_name} - {user.birthday}')
        elif option == '5':
            print('Exit')
            break
        else:
            print('Invalid option')
        print()
