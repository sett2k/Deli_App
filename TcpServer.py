import socket
import threading
import FetchData
# import pymongo
from database import Deliver

obj = Deliver()


class TCPServer:
    def __init__(self):
        self.sock = None
        self.server_ip = "localhost"
        self.server_port = 9998
        # self.Server_Sms = bytes(Server_Sms, 'utf-8')

    def main(self):
        server_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_1.bind((self.server_ip, self.server_port))
        server_1.listen(6)
        print(f'Server listen on {self.server_ip}, Port:{self.server_port}')
        # server_1.send(self.Server_Sms)

        while True:
            cleint, address = server_1.accept()
            print(f'Accepted connection from {address[0]} : {address[1]}')
            cleint_handler = threading.Thread(target=self.handle_client, args=(cleint,))
            cleint_handler.start()

    def handle_client(self, client_socket):
        with client_socket as sock:
            global request
            request = sock.recv(1024)
            toFindInDatabase = request.decode()
            print('Received Data From Client:', toFindInDatabase)
            # print(type(deli.data_o()))
            if toFindInDatabase == '1':
                return_r = obj.showMenu()
                sock.send(return_r.encode())
                self.order(sock)
            elif toFindInDatabase == '2':
                self.create_Acc(sock)
            elif toFindInDatabase == '3':
                self.sign_in(sock)

    def create_Acc(self, socket_client):
        with socket_client as sock:
            send_b = obj.create_Str()
            sock.send(send_b.encode())
            receive = sock.recv(1024).decode()
            print("Received data :", receive)
            receive_1 = receive.split(',')
            print(receive_1)
            num = obj.checkPh(int(receive_1[0]))
            if num == 2:
                if len(receive_1[2]) >= 8:
                    if receive_1[2] != receive_1[3]:
                        temp = 'Check Your Password Again!!'
                        sock.send(temp.encode())
                        self.create_Acc(socket_client)
                    else:
                        id1 = obj.collection_2.find().distinct('_id')
                        i = len(id1)
                        obj.collection_2.insert_one({'_id': id1[i - 1] + 1, 'Username': receive_1[1], 'Password':
                            receive_1[2], 'PhoneNumber': int(receive_1[0]), 'Address': receive_1[4]})
                        print("Data Inserted.")
                        # send_s = self.sign_in_Str()
                        # sock.send(send_s.encode())
                        self.sign_in(sock)
                else:
                    temp3 = 'Password must have at least 8 counts.'
                    sock.send(temp3.encode())
                    self.create_Acc(socket_client)
            else:
                temp2 = "Invalid PhoneNumber!!\nPls start with '959' and enter total '9' numbers."
                sock.send(temp2.encode())
                self.create_Acc(socket_client)

    def sign_in(self, socket_client):
        with socket_client as sock:
            send_input = obj.sign_in_Str()
            sock.send(send_input.encode())
            rec_input = sock.recv(1024).decode()
            print("Received data :", rec_input)
            rec_list = rec_input.split(',')
            print(rec_list)
            num = obj.checkPh(int(rec_list[0]))
            if num == 3:
                num2 = obj.check_pass(int(rec_list[0]), rec_list[1])
                if num2 == 1:
                    print('Sign-in Success.')
                    menu = obj.showMenu()
                    sock.send(menu.encode())
                    self.order(sock)
                else:
                    print('Check Password.')
                    self.sign_in(socket_client)
            else:
                print('Invalid Number.')
                self.sign_in(socket_client)

    def order(self, socket_client):
        with socket_client as sock:
            send_option = "\nPress '1' to pick menu.\nPress '2' to drop menu.\nPress '3' to confirm order.\n" \
                        "Press '4' to cancel order.\nEnter your option :"
            sock.send(send_option.encode())
            rec_option = sock.recv(1024).decode()
            # if 'done' in rec_menu:
            print("Received option :", rec_option)
            if '1' in rec_option:
                total_list = []
                while True:
                    print('while loop.')
                    send_menu = "Choose your menu. Type 'done' if you've finished :"
                    sock.send(send_menu.encode())
                    rec_menu = sock.recv(1024).decode()
                    print(rec_menu)
                    if 'done' in rec_menu:
                        check = obj.total_cost(total_list, 'Prepaid')
                        print(type(check))
                        sock.send(check.encode())
                        print(check)
                        break
                    else:
                        menu_check = obj.check_menu(rec_menu)
                        if 'none' in menu_check:
                            print('Your item is unavailable.')
                            # self.order(socket_client)
                        else:
                            print('Your item is available.')
                            menu_check = 'Menu available...\n' + menu_check
                            sock.send(menu_check.encode())
                            send_order = obj.order_Str()
                            sock.send(send_order.encode())
                            rec_order = sock.recv(1024).decode()
                            list_order = rec_order.split(',')
                            list_order.append(list_order[1])
                            list_order[1] = rec_menu
                            total_list.append(list_order)
                            print(list_order)
                            price = obj.count_cost(list_order[0], list_order[1], list_order[2])
                            sock.send(price.encode())
                print('break')
            elif '2' in rec_option:
                print('2')
            elif '3' in rec_option:
                print('3')
            elif '4' in rec_option:
                print('4')
            # else:
            #     self.order(sock)

    def to_Find(self, toFindInDatabase):
        db = FetchData.DatabaseClass(toFindInDatabase)
        DBdata = db.databaseMethod()
        return DBdata


if __name__ == "__main__":
    while True:
        # server_sms = input("Enter message to send back to Client :")
        server = TCPServer()
        server.main()

# order check
# if not done, can order continuously
# count cost error
# split order function if needed
# add to cart
