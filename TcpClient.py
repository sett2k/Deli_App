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
        self.client.send(option.encode())
        receive = self.client.recv(1024).decode()
        if '$' in receive:
            print('Account Creating Session...')
            self.create(receive, '$')
        elif '*' in receive:
            print('Sign-In Session...')
            self.sign_in(receive, '*')
        else:
            print('______ Our Menu-Book ______')
            print(receive)
            self.order()
        self.client.close()

    def create(self, rec_input, a):
        str_input = obj.splitData(rec_input, a)
        self.client.send(str_input.encode())
        reason = self.client.recv(1024).decode()
        rec_check = self.client.recv(1024).decode()
        if rec_check == rec_input:
            print(reason)
            self.create(rec_check, a)
        else:
            print("Registration Complete.\nPls sign in to use our app.")
            # print(rec, '\n', rec_2, '\n', rec_3)
            self.sign_in(rec_check, '*')

    def sign_in(self, rec_input, a):
        send_input = obj.splitData(rec_input, a)
        self.client.send(send_input.encode())
        rec_check = self.client.recv(1024).decode()
        if rec_check == rec_input:
            print('try again.')
            self.sign_in(rec_check, a)
        else:
            print('Signed-in Success.\n_____ Our Menu _____')
            print(rec_check)
            # rec_input2 = self.client.recv(1024).decode()
            self.order()

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
