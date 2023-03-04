import json

import pymongo


class Deliver:
    try:
        connection = pymongo.MongoClient("localhost", 27017)
        database = connection['Database']
        collection = database['Menu Book']
        collection_2 = database['User-Data']
    except Exception as error:
        print(error)

    def __init__(self):

        data = [
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

        data_2 = [
            {"_id": 1, "Username": "One", "Password": "one#1234", "PhoneNumber": 95911111111, "Address": "OneCity"},
            {"_id": 2, "Username": "Two", "Password": "two#1234", "PhoneNumber": 959222222222, "Address": "TwoCity"},
            {"_id": 3, "Username": "Three", "Password": "three#12", "PhoneNumber": 959333333333,
             "Address": "ThreeCity"}
        ]
        # try:
        #     self.collection.insert_many(data)
        #     self.collection.insert_many(data_2)
        #     print('Data Inserted.')
        # except Exception as error:
        #     print(error)

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
        menu += 'You can order now...'
        return menu

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

    def total_cost(self, total_list, payment):
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
            menu_list += list_i[2] + ' * ' + list_i[1] + '(' + str(price) + ') = ' + str(cost) + '\n'
        deli_fee = 3000
        total += deli_fee
        deli_fee2 = 'Deli fees = ' + str(deli_fee) + '\n'
        payment_type = "Payment Type >> '" + payment + "'\n"
        menu = '......dailY deli......\n'
        menu += menu_list + deli_fee2 + 'Total cost = ' + str(total) + '\n' + payment_type + '--- THANK YOU FOR ' \
                                                                                             'SUPPORTING US! ---'
        return menu

    def create_Str(self):
        # create = self.collection_2.distinct('Address')
        c_input = 'Enter Your PhoneNumber :$Enter Your Username    :$Enter Your Password    :' \
                  '$Confirm Your Password  :$Enter Your Address     :'
        return c_input

    def sign_in_Str(self):
        s_input = 'Enter Your PhoneNumber :*Enter Your Password    :'
        return s_input

    def order_Str(self):
        o_input = 'Choose Shop Name :&Enter the item count :'
        return o_input

# obj.showMenu()
# count cost error - line 105
