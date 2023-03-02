class Function:
    def intro(self):

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
            self.intro()

    def splitData(self, rec, a):
        r_list = rec.split(a)
        s_list = []
        for i in r_list:
            temp = input(i)
            s_list.append(temp)

        strS = ','.join(map(str, s_list))
        return strS
