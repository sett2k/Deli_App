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
            send_s = obj.sign_in_Str()
            sock.send(send_s.encode())
            rec = sock.recv(1024).decode()
            print("Received data :", rec)
            rec1 = rec.split(',')
            print(rec1)
            num = obj.checkPh(int(rec1[0]))
            if num == 3:
                num2 = obj.check_pass(int(rec1[0]), rec1[1])
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
            send_o = 'Choose Your Menu :'
            sock.send(send_o.encode())
            rec = sock.recv(1024).decode()
            print("Received data :", rec)
            str_order = obj.check_menu(rec)
            if 'none' in str_order:
                print('Your item is unavailable.')
                self.order(socket_client)
            else:
                print('Your item is available.')
                str_order = 'Menu available...\n' + str_order
                sock.send(str_order.encode())
                send_order = obj.order_Str()
                sock.send(send_order.encode())
                rec1 = sock.recv(1024).decode()
                list1 = rec1.split(',')
                print(list1)
                num = obj.count_cost(rec)
                if num != -1:
                    cost = rec + "'s cost = " + str(num)
                    count = '\n' + 'Count = ' + list1[1]
                    total = '\n' + 'Total cost = ' + str(num * int(list1[1]))
                    send_cost = cost + count + total
                    sock.send(send_cost.encode())
                else:
                    print('invalid.')


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
# count cost
# split order function if needed
