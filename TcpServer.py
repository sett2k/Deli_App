import socket
import threading
# import pymongo
from database import Deliver

obj = Deliver()
total_list = []


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
            request = sock.recv(1024)
            toFindInDatabase = request.decode()
            print('Received Data From Client:', toFindInDatabase)
            # print(type(deli.data_o()))
            if toFindInDatabase == '1':
                return_r = obj.showMenu()
                sock.send(return_r.encode())
                order = '\nOrder Session...@'
                self.order(sock, order)
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
                                                    receive_1[2], 'PhoneNumber': int(receive_1[0]),
                                                     'Address': receive_1[4], 'Record': 0, "Sign-in": 0})
                        print("Data Inserted.")
                        send1 = 'Account successfully created.\n'
                        sock.send(send1.encode())
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
            print(send_input)
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
                    obj.record_sign_in(int(rec_list[0]))
                    # phNo = obj.collection_2.find().distinct('PhoneNumber')
                    # for i in phNo:
                    #     if int(rec_list[0]) == i:
                    #         data = obj.collection_2.find_one({'PhoneNumber': i})
                    #         sign_in = data.get('Sign-in')
                    #         sign_in += 1
                    menu = obj.showMenu()
                    sock.send(menu.encode())
                    str1 = ''
                    self.order(sock, str1)
                else:
                    print('Check Password.')
                    self.sign_in(socket_client)
            else:
                print('Invalid Number.')
                self.sign_in(socket_client)

    def order(self, socket_client, str_order):
        with socket_client as sock:
            send_option = "Press '1' to pick menu.\nPress '2' to update menu.\nPress '3' to confirm order.\n" \
                          "Press '4' to cancel order.\nPress '5' to exit.\nEnter your option :"
            send_option = str_order + send_option
            sock.send(send_option.encode())
            rec_option = sock.recv(1024).decode()
            print("Received option :", rec_option)
            # total_list = []
            print('Total List :', total_list)
            if '1' in rec_option:
                self.pick_menu(sock)
            elif '2' in rec_option:
                self.update_menu(sock)
            elif '3' in rec_option:
                self.confirm_order(sock)
            elif '4' in rec_option:
                length = len(total_list)
                if length != 0:
                    for i in range(len(total_list)):
                        total_list.pop(0)
                    cancel = 'Order Cancelled!'
                    cancel += '\nYour Menu Chart >> \n' + '\n'.join(map(str, total_list)) + '@'
                else:
                    cancel = "You haven't chosen any menu yet!!@\n"
                self.order(sock, cancel)
            elif '5' in rec_option:
                print('Client disconnected.')
            else:
                recall = 'Invalid Option!!@'
                self.order(sock, recall)

    def pick_menu(self, socket_client):
        with socket_client as sock:
            reply = str()
            send_menu = reply + "Choose your menu  :"
            sock.send(send_menu.encode())
            rec_menu = sock.recv(1024).decode()
            # print(rec_menu)
            menu_check = obj.check_menu(rec_menu)
            if 'none' in menu_check:
                print('Your item is unavailable.')
                reply = 'Your item is unavailable.@\n'
                self.order(sock, reply)
            else:
                print('Your item is available.')
                menu_check = 'Menu available...\n' + menu_check
                # sock.send(menu_check.encode())
                send_order = obj.order_Str()
                send_order = menu_check + '@' + send_order
                sock.send(send_order.encode())
                rec_order = sock.recv(1024).decode()
                list_order = rec_order.split(',')
                list_order.append(list_order[1])
                list_order[1] = rec_menu
                shop_check = obj.check_shop(list_order)
                if shop_check == 'present':
                    count = 0
                    for list_m in total_list:
                        if list_order[1].title() == list_m[1] and list_order[0].upper() == list_m[0]:
                            count1 = int(list_order[2])
                            count2 = int(list_m[2])
                            count1 += count2
                            list_m[2] = str(count1)
                            count = 1
                            break
                        else:
                            count = 0
                    if count == 0:
                        total_list.append(list_order)
                    print(list_order)
                    print(total_list)
                    price = obj.count_cost(list_order[0], list_order[1], list_order[2])
                    sock.send(price.encode())
                    menu_chart = obj.menu_list(total_list)
                else:
                    menu_chart = 'Invalid Shop Name!!@\n'
                self.order(sock, menu_chart)

    def update_menu(self, socket_client):
        with socket_client as sock:
            print('def.')
            length = len(total_list)
            if length != 0:
                list_to_str = '\n'.join(map(str, total_list))
                drop = list_to_str + '@Choose the menu you want to edit :&Enter the shop name        :&' \
                                     'Enter the number of menu item    :'
                sock.send(drop.encode())
                rec_drop = sock.recv(1024).decode()
                drop_list = rec_drop.split(',')
                print(drop_list)
                length = len(total_list)
                for i in range(length):
                    print('a')
                    title1 = total_list[i][0].upper()
                    title2 = total_list[i][1].title()
                    if title2 == drop_list[0].title() and title1 == drop_list[1].upper():
                        total_list[i][2] = drop_list[2]
                        if int(total_list[i][2]) <= 0:
                            total_list.pop(i)
                        sock_str = "Menu Updated.\n"
                        menu_chart = obj.menu_list(total_list)
                        sock_str += menu_chart
                        break
                    else:
                        sock_str = 'Menu not found.\n'
                print(total_list, '\n', sock_str)
                self.order(sock, sock_str)
            else:
                print(total_list)
                sock_str = "You haven't chosen any menu yet!!@\n"
                self.order(sock, sock_str)

    def confirm_order(self, client_socket):
        with client_socket as sock:
            length = len(total_list)
            if length != 0:
                location = 'Enter the address       :'
                sock.send(location.encode())
                location_reply = sock.recv(1024).decode()
                phoneNo = 'Enter your Phone Number :'
                sock.send(phoneNo.encode())
                phNumber = sock.recv(1024).decode()
                phNo = int(phNumber)
                if 959999999999 >= phNo > 959100000000:
                    print(location_reply, phNo)
                    payment_option = "Choose your payment type.\n'1' for 'Prepaid'. // '2' for 'Cash-On-Deli'.\n"
                    sock.send(payment_option.encode())
                    while True:
                        rec_option = sock.recv(1024).decode()
                        if rec_option == '1':
                            payment = "Transfer to this number.\n'09978652431' - KBZPay/WavePay/CBPay/AYAPay\n" \
                                           "Type 'done' if you've transferred.\n"
                            sock.send(payment.encode())
                            rec_done = sock.recv(1024).decode()
                            if 'done' in rec_done:
                                check = obj.total_cost(total_list, 'Prepaid', phNo)
                                sock.send(check.encode())
                                break
                            else:
                                reply = 'Pls Transfer the amount first!!!\n'
                                reply += payment_option
                                sock.send(reply.encode())
                        else:
                            check = obj.total_cost(total_list, 'Cash-On-Deli', phNo)
                            sock.send(check.encode())
                            break
                    for i in range(len(total_list)):
                        total_list.pop(0)
                    order = 'Order Confirmed.@\n'
                    sign = obj.collection_2.find().distinct('Sign-in')
                    for i in sign:
                        if i > 0:
                            sign_in = obj.collection_2.find_one({'Sign-in': i})
                            record = sign_in.get('Record')
                            record += 1
                else:
                    order = 'Invalid Phone Number!!@\n'
                print(total_list)
            else:
                order = "You haven't chosen any menu yet!!@\n"
            self.order(sock, order)


if __name__ == "__main__":
    while True:
        server = TCPServer()
        server.main()

# edit menu count (clear)
# if choose same menu, must add to former menu count (clear)
# error - same menus don't add & show twice (clear)
# false shop name error (clear)
# confirm order error - no menu pick (clear)
# cancel order error - no menu  (clear)
# show shop name on check (clear)
# update menu error - only update first menu, add shop name in menu check (clear)
# add order history - note sign-in acc and use sign-in acc in order confirm function and plus one to record
# add delivery men accounts
# add admin accounts
# add date to check
# back functions for client
# input validation for every function

# specify Classes
# modify database
