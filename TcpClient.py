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
            menu_input = self.client.recv(1024).decode()
            self.order(menu_input)
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
            self.sign_in(reason, '*')

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
            rec_input2 = self.client.recv(1024).decode()
            self.order(rec_input2)

    def order(self, rec_input):
        send_option = input(rec_input)
        self.client.send(send_option.encode())
        print(send_option)
        while True:
            print('while loop.')
            print(send_option)
            menu_pick = self.client.recv(4096).decode()
            # menu_pick2 = self.client.recv(1024).decode()
            print(menu_pick)
            send_menu = input(menu_pick)
            self.client.send(send_menu.encode())
            print(send_menu)
            if 'done' in send_menu:
                rec_check = self.client.recv(1024).decode()
                print(rec_check)
                break
            else:
                menu_check = self.client.recv(1024).decode()
                if menu_check != menu_pick:
                    print(menu_pick)
                    print(menu_check)
                    rec_order = self.client.recv(1024).decode()
                    send_order = obj.splitData(rec_order, '&')
                    self.client.send(send_order.encode())
                    rec_price = self.client.recv(1024).decode()
                    print('\n' + rec_price)
                    # print('Your order is confirmed.')
                else:
                    print('Your item is unavailable.')
                    self.order(menu_pick)


if __name__ == "__main__":
    # clientMessage = input("Enter message to send:>")
    print("+======== WELCOME TO dailY deli =========+")
    ClientConnector = Client()
    ClientConnector.runClient()
