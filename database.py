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
             "Record": 0, "Sign-in": 0},
            {"_id": 2, "Username": "Two", "Password": "two#1234", "PhoneNumber": 959222222222, "Address": "TwoCity",
             "Record": 0, "Sign-in": 0},
            {"_id": 3, "Username": "Three", "Password": "three#12", "PhoneNumber": 959333333333,
             "Address": "ThreeCity", "Record": 0, "Sign-in": 0}
        ]

        history = [{"PhoneNumber": int(), "History": [{"shop name": "Barlala"}]}]

        try:
            #     #     self.Menu_Book.insert_many(menu)
            #     #     self.User_Data.insert_many(user_info)
            query = {"shop name": "Barlala"}
            self.History.insert_many(history)
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

    def Ph_valid_check(self, phNo):
        count = 0
        for i in phNo:
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
                if j.title() == item.title():
                    menu_dict = self.collection.find_one({'Menu': i})
                    shop_name = menu_dict.get('Shop Name')
                    price = i.get(item.title())
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
                if j == order[1].title():
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
            menu_list += list_i[2] + ' * ' + list_i[1] + '(' + str(price) + ') -> "' + list_i[0] + '" = ' + str(
                cost) + '\n'
        deli_fee = 3000
        total += deli_fee
        deli_fee2 = 'Deli fees = ' + str(deli_fee) + '\n'
        payment_type = "Payment Type >> '" + payment + "'\n"
        deli = '......dailY deli......\n'
        x = datetime.datetime.now()
        date = x.strftime("%d/%b/%Y__%I:%M:%S-%p")
        date = 'Order date    : ' + date
        phNo = "\nCustomer's Ph : " + str(phoneNo) + '\n'
        menu = deli + date + phNo + menu_list + deli_fee2 + 'Total cost = ' + str(total) + '\n' + payment_type + '--- THANK YOU ' \
                                                                                                    'FOR SUPPORTING ' \
                                                                                                    'US! --- '
        return menu

    def record_sign_in(self, phNo):
        phNumber = self.collection_2.find().distinct('PhoneNumber')
        for i in phNumber:
            if phNo == i:
                data = self.collection_2.find_one({'PhoneNumber': phNo})
                sign_in = data.get('Sign-in')
                original_rec = {'Sign-in': sign_in}
                updated_rec = {'$set': {'Sign-in': sign_in + 1}}
                self.collection_2.update_one(original_rec, updated_rec)

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
