from client_Fun import Function

obj = Function()


# for i in range(11):
#     if i == 6:
#         break
#     else:
#         print(i)


def test():
    count = 0
    option = intro()
    list_option = ['1', '2', '3']
    for p in list_option:
        if p == option:
            count = 1
            break
        else:
            count = 0
    if count == 0:
        test()
    print('Option -', option)


def intro():
    print("Press '1' to show menu.")
    print("Press '2' to create an account.")
    print("Press '3' to log in your account.")
    print("Press '4' to exit.")
    key = input()
    if key == '1':
        return key
    elif key == '2':
        return key
    elif key == '3':
        return key
    elif key == '4':
        exit(1)
    else:
        print('Invalid Option.')
        return key


if __name__ == '__main__':
    test()
