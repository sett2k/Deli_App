import socket
from client_Fun import Function

obj = Function()


class Client:
    def __init__(self):
        self.target_host = 'localhost'
        self.target_port = 9998
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.target_host, self.target_port))
        # self.ClientMessage = bytes(ClientMessage, 'utf-8')

    def runClient(self):
        option = obj.intro()
        count = 0
        option_list = ['1', '2', '3']
        for i in option_list:
            if i == option:
                count = 1
                break
        if count == 0:
            self.runClient()
        self.client.send(option.encode())
        if option == '1':
            receive = self.client.recv(1024).decode()
            print('______ Our Menu-Book ______')
            print(receive)
            self.order()
        elif option == '2':
            self.create()
        elif option == '3':
            self.sign_in()

        # if '$' in receive:
        #     print('Account Creating Session...')
        #     self.create()
        # elif '*' in receive:
        #     print('Sign-In Session...')
        #     self.sign_in(receive, '*')
        # else:

        self.client.close()

    def create(self):
        rec_input = self.client.recv(1024).decode()
        if '@\n' in rec_input:
            rec_list = rec_input.split('@\n')
            print(rec_list[0])
            rec_list.pop(0)
            rec_input = str()
            rec_input = rec_input.join(rec_list)
        elif '*' in rec_input:
            self.sign_in()
        str_input = obj.splitData(rec_input, '$')
        self.client.send(str_input.encode())
        if 'back' in str_input:
            self.create()
        if 'exit' in str_input:
            self.runClient()
        self.create()

    def sign_in(self):
        rec_input = self.client.recv(1024).decode()
        print(rec_input)
        if '@\n' in rec_input:
            rec_list = rec_input.split('@\n')
            print(rec_list[0])
            rec_list.pop(0)
            rec_input = str()
            rec_input = rec_input.join(rec_list)
        elif 'Order' in rec_input:
            self.order()
        send_input = obj.splitData(rec_input, '*')
        self.client.send(send_input.encode())
        self.sign_in()

    def order(self):
        while True:
            rec_input = self.client.recv(1024).decode()
            if 'cost' in rec_input:
                print(rec_input)
                self.order()
            elif rec_input == 'exit':
                self.runClient()
            else:
                if '@' in rec_input:
                    rec_list = rec_input.split('@')
                    # print(rec_list)
                    print(rec_list[0])
                    del rec_list[0]
                    list_to_str = str()
                    list_to_str = list_to_str.join(rec_list)
                    rec_input = list_to_str

                send_input = obj.splitData(rec_input, '&')
                # print(send_input)
                self.client.send(send_input.encode())


if __name__ == "__main__":
    # clientMessage = input("Enter message to send:>")
    print('+======== WELCOME TO "dailY deli" =========+')
    ClientConnector = Client()
    ClientConnector.runClient()

# invalid option
