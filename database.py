import json

import pymongo

import datetime


class Deliver:
    try:
        connection = pymongo.MongoClient("localhost", 27017)
        database = connection['Database']
        collection = database['Menu Book']
        collection_2 = database['User-Data']
        History = database['Order History']
        Deli_Men = database['Deli-Men']
    except Exception as error:
        print(error)

    def __init__(self):

        menu = [
            {"_id": 1, "Shop Name": "Barlala", "Menu": {"Beer": 2000, 'Colds': 1500, 'Juices': 1500, 'BBQ': 10000,
                                                        'Hotpot': 8000, 'Salads': 2000, 'Fried Snacks': 2500,
                                                        'Beverages': 2000}},
            {"_id": 2, "Shop Name": "Pan Ei",
             "Menu": {"Tea Leaf Salad": 2000, 'Popcorn Salad': 2000, 'Ginger Salad': 2000, 'Pennyworth Salad': 2000,
                      "Tomato Salad": 2000}, "Drink": {'Lemon': 500, 'Apple': 15000}},
            {"_id": 3, "Shop Name": "THU TASTY",
             "Menu": {"Lemon": 1500, 'Lime': 1500, 'Orange': 1500, 'Strawberry': 1500, 'Aml': 1500, 'Grape': 1500,
                      'Apple': 1500, 'Pineapple': 1500, "Watermelon": 1500, 'Bubble Tea': 2000}},
            {"_id": 4, "Shop Name": "Lotteria", "Menu": {"Fried Chicken": 2500, 'Burger': 3000, 'Cola': 1000,
                                                         'Fries': 1500, "Rice-Box": 1000, 'Pizza': 8000}}]

        user_info = [
            {"_id": 1, "Username": "One", "Password": "one#1234", "PhoneNumber": 95911111111, "Address": "OneCity",
             "Transfer-Record": '', "Sign-in": 0},
            {"_id": 2, "Username": "Two", "Password": "two#1234", "PhoneNumber": 959222222222, "Address": "TwoCity",
             "Record": '959222222222', "Sign-in": 0},
            {"_id": 3, "Username": "Three", "Password": "three#12", "PhoneNumber": 959333333333,
             "Address": "ThreeCity", "Record": '959333333333', "Sign-in": 0}
        ]

        # history = [{"_id": 1, "PhoneNumber": int(), "Order-History": ""}]

        try:
            #     #     self.Menu_Book.insert_many(menu)
            #     #     self.User_Data.insert_many(user_info)
            # query = {"shop name": "Barlala"}
            # self.History.insert_many(history)
            print('Data Inserted.')
        except Exception as error:
            print(error)

    def showMenu(self):
        shop = self.collection.find().distinct('Shop Name')
        shop_s = '", "'.join(map(str, shop))
        shop_l = shop_s.split('", "')
        menu = 'Food Stores >> "' + shop_s + '"'
        for i in shop_l:
            shop_name = self.collection.find_one({'Shop Name': i})
            shop_dict = shop_name.get('Menu')
            shop_menu = str()
            for key in shop_dict:
                shop_menu += key + ' - ' + str(shop_dict[key]) + '\n'
            shop_menu = 'MENU available at ' + i + '....' + '\n' + shop_menu
            menu = menu + '\n' + shop_menu
        menu += '!You can order now!'
        return menu

    def num_valid_check(self, num):
        count = 0
        for i in num:
            if 48 <= ord(i) <= 57:
                count += 1
            else:
                count = 0
                break
        return count

    def checkPh(self, phNo):
        b = 0
        if 959999999999 >= phNo > 959111111110:
            a = 2
        else:
            a = 0
        find = self.collection_2.find().distinct('PhoneNumber')
        for i in find:
            if phNo == i:
                b = 1
                break
            else:
                b = 0
        num = a + b
        return num

    def check_pass(self, phNo, s_pass):
        c_dict = self.collection_2.find_one({'PhoneNumber': phNo})
        c_pass = c_dict.get('Password')
        if c_pass == s_pass:
            return 1
        else:
            return -1

    def check_menu(self, item):
        menu = self.collection.find().distinct('Menu')
        shop_list = []
        price_list = []
        count = 0
        menu_str = str()
        for i in menu:
            for j in i:
                if j.upper() == item.upper():
                    menu_dict = self.collection.find_one({'Menu': i})
                    shop_name = menu_dict.get('Shop Name')
                    price = i.get(j)
                    shop_list.append(shop_name)
                    price_list.append(price)
                    menu_list = zip(shop_list, price_list)
                    menu_str = json.dumps(dict(menu_list))
                    count += 1
                else:
                    count += 0
        if count > 0:
            return menu_str
        else:
            return 'none'

    def check_shop(self, order):
        menu = self.collection.find().distinct('Menu')
        reply = str()
        for i in menu:
            for j in i:
                if j.upper() == order[1].upper():
                    whole_menu = self.collection.find_one({'Menu': i})
                    shop = whole_menu.get('Shop Name')
                    print(whole_menu)
                    print(shop)
                    if shop == order[0].upper():
                        return 'present'
                    else:
                        reply = 'absent'
        return reply

    def count_cost(self, shop, item, number):
        shop1 = shop.upper()
        item1 = item.title()
        menu_str = self.check_menu(item1)
        menu_dict = json.loads(menu_str)
        price = menu_dict.get(shop1)
        # count = str()
        item_cost = price * int(number)
        cost = item1 + "'s cost = " + str(price)
        count = '\nCount = ' + number
        total = '\nTotal cost = ' + str(item_cost)
        cost += count + total
        return cost

    def total_cost(self, total_list, payment, phoneNo):
        total = 0
        menu_list = str()
        for list_a in total_list:
            for b in range(len(list_a)):
                if b == 0:
                    list_a[b] = list_a[b].upper()
                else:
                    list_a[b] = list_a[b].title()

        for list_i in total_list:
            menu_str = self.check_menu(list_i[1])
            menu_dict = json.loads(menu_str)
            price = menu_dict.get(list_i[0])
            cost = price * int(list_i[2])
            total += cost
            menu_list += "'" + list_i[0] + "' -> " + list_i[2] + ' * ' + list_i[1] + '(' + str(price) + ') = ' + str(
                cost) + '\n'
        deli_fee = 3000
        total_fee = total + deli_fee
        deli_fee2 = '\nDeli fees = ' + str(deli_fee) + '\n'
        payment_type = "Payment Type >> '" + payment + "'\n"
        deli = '......dailY deli......\n'
        x = datetime.datetime.now()
        date = x.strftime("%d/%b/%Y__%I:%M:%S_%p")
        date = 'Order date    : ' + date
        phNo = "\nCustomer's Ph : " + str(phoneNo) + '\n'
        menu = deli + date + phNo + menu_list + 'Total = ' + str(total) + deli_fee2 + 'Total cost = ' + str(
            total_fee) + '\n' + payment_type + '--- THANK YOU ' \
                                               'FOR SUPPORTING ' \
                                               'US! --- '
        return menu

    def transfer_record(self, sum_list, phNum):
        cash = self.total_cost(sum_list, 'Prepaid', phNum)
        cash_list = cash.split('\n')
        x = datetime.datetime.now()
        date = x.strftime("%d/%b/%Y__%I:%M:%S_%p")
        amount = ''
        for i in range(len(cash_list)):
            if 'Total cost' in cash_list[i]:
                total = cash_list[i].split(' = ')
                amount = total[1]
                break
        admin_doc = self.collection_2.find_one({'_id': 1})
        transfer = admin_doc.get('Transfer-Record')
        phoneNum = str(phNum)
        update = transfer + '\n' + phoneNum + '-' + amount + '-' + date
        original_transfer = {'Transfer-Record': transfer}
        updated_transfer = {'$set': {'Transfer-Record': update}}
        self.collection_2.update_one(original_transfer, updated_transfer)
        print('Transfer Record Updated.')

    def record_sign_in(self, phNo):
        phNumber = self.collection_2.find().distinct('PhoneNumber')
        for i in phNumber:
            if phNo == i:
                data = self.collection_2.find_one({'PhoneNumber': phNo})
                sign_in = data.get('Sign-in')
                original_value = {'Sign-in': sign_in}
                updated_value = {'$set': {'Sign-in': sign_in + 'sign-in'}}
                self.collection_2.update_one(original_value, updated_value)
                print('Sign-in updated.')

    def delete_signin_record(self):
        phoneNo = self.collection_2.find().distinct('PhoneNumber')
        for i in phoneNo:
            data = self.collection_2.find_one({'PhoneNumber': i})
            sign_value = data.get('Sign-in')
            original_value = {'Sign-in': sign_value}
            updated_value = {'$set': {'Sign-in': str(i)}}
            self.collection_2.update_one(original_value, updated_value)
        print('Sign-in record deleted.')

    def record_order(self, phNo, list_total, payment):
        count = 0
        sign_rec = self.collection_2.find().distinct('Sign-in')
        for i in sign_rec:
            if 'sign-in' in i:
                doc = self.collection_2.find_one({'Sign-in': i})
                record = doc.get('Record')
                original_rec = {'Record': record}
                order_check = self.total_cost(list_total, payment, phNo)
                updated_rec = {'$set': {'Record': record + '@\n\n' + order_check}}
                self.collection_2.update_one(original_rec, updated_rec)
                print('Sign-in record updated.')
                return 1
            else:
                print('no record updated.')
        return count

    def record_order_2(self, phoneNo, list_total, pay_type):
        count = 0
        phoneNum = self.collection_2.find().distinct('PhoneNumber')
        order_id = self.History.find().distinct('_id')
        # i = len(order_id)
        bill = self.total_cost(list_total, pay_type, phoneNo)
        for i in phoneNum:
            if phoneNo == i:
                ph_doc = self.collection_2.find_one({'PhoneNumber': phoneNo})
                record = ph_doc.get('Record')
                original_record = {'Record': record}
                updated_record = {'$set': {'Record': record + '@\n\n' + bill}}
                self.collection_2.update_one(original_record, updated_record)
                print('Sign-in record updated.')
                count = 1
                break
            else:
                count = 0
        if count == 0:
            sum_up = 0
            phNumber = self.History.find().distinct('PhoneNumber')
            for j in phNumber:
                if j == phoneNo:
                    doc_ph = self.History.find_one({'PhoneNumber': phoneNo})
                    history = doc_ph.get('Order-History')
                    original_history = {'Order-History': history}
                    updated_history = {'$set': {'Order-History': history + '@\n\n' + bill}}
                    self.History.update_one(original_history, updated_history)
                    print('No-sign-in same record updated.')
                    sum_up = 1
                    break
                else:
                    sum_up = 0
            if sum_up == 0:
                self.History.insert_one({'_id': order_id[-1] + 1, 'PhoneNumber': phoneNo, 'Order-History': bill})
                print('No-sign-in different record updated.')

    def record_deli(self, cusPh, menu_list, pay_ment):
        deli_bill = self.total_cost(menu_list, pay_ment, cusPh)
        deli_ph = self.Deli_Men.find().distinct('PhoneNumber')
        for i in deli_ph:
            deli_doc = self.Deli_Men.find_one({'PhoneNumber': i})
            deli_req = deli_doc.get('Customer-Request')
            original_req = {'Customer-Request': deli_req}
            updated_req = {'$set': {'Customer-Request': deli_req + '@\n\n' + deli_bill}}
            self.Deli_Men.update_one(original_req, updated_req)
            duty = deli_doc.get('Duty-Record')
            original_duty = {'Duty-Record': duty}
            updated_duty = {'$set': {'Duty-Record': duty + '@\nduty'}}
            self.Deli_Men.update_one(original_duty, updated_duty)
            print('Deli-record updated.')

    def menu_list(self, list_menu):
        for list_i in list_menu:
            list_i[0] = list_i[0].upper()
            list_i[1] = list_i[1].title()
        reply = '___Your Menu Chart___ \n' + '\n'.join(map(str, list_menu)) + '@\n'
        return reply

    def create_Str(self):
        c_input = 'Enter Your PhoneNumber :$Enter Your Username    :$Enter Your Password    :' \
                  '$Confirm Your Password  :$Enter Your Address     :'
        return c_input

    def sign_in_Str(self):
        s_input = 'Enter Your PhoneNumber :*Enter Your Password    :'
        return s_input

    def order_Str(self):
        o_input = 'Choose Shop Name     :&Enter the item count :'
        return o_input
