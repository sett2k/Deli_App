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
        self.client.close()

    def create(self, rec, a):
        str1 = obj.splitData(rec, a)
        self.client.send(str1.encode())
        rec_2 = self.client.recv(1024).decode()
        rec_3 = self.client.recv(1024).decode()
        if rec_3 == rec:
            print(rec_2)
            self.create(rec_3, a)
        else:
            print("Registration Complete.\nPls sign in to use our app.")
            # print(rec, '\n', rec_2, '\n', rec_3)
            self.sign_in(rec_2, '*')

    def sign_in(self, rec, a):
        str1 = obj.splitData(rec, a)
        self.client.send(str1.encode())
        rec1 = self.client.recv(1024).decode()
        if rec1 == rec:
            print('try again.')
            self.sign_in(rec1, a)
        else:
            print('Signed-in Success.\n_____ Our Menu _____')
            print(rec1)
            rec2 = self.client.recv(1024).decode()
            self.order(rec2)

    def order(self, rec):
        send_menu = input(rec)
        self.client.send(send_menu.encode())
        rec2 = self.client.recv(1024).decode()
        if rec2 != rec:
            print(rec2)
            rec3 = self.client.recv(1024).decode()
            str2 = obj.splitData(rec3, '&')
            self.client.send(str2.encode())
            rec_cost = self.client.recv(1024).decode()
            print('\n' + rec_cost)
            print('Your order is confirmed.')
        else:
            print('Your item is unavailable.')
            self.order(rec2)


if __name__ == "__main__":
    # clientMessage = input("Enter message to send:>")
    print("+======== WELCOME TO dailY deli =========+")
    ClientConnector = Client()
    ClientConnector.runClient()
