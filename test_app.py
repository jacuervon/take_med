from test.test_users import test_user_model, test_create, test_get_by_id, test_get_all, test_delete


def main():
    test_user_model()
    test_create()
    test_get_by_id()
    test_get_all()
    test_delete()


if __name__ == '__main__':
    main()
