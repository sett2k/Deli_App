# import json
#
# from database import Deliver
#
# obj = Deliver()
#
#
# def check():
#     menu = obj.collection.find().distinct('Menu')
#     # print(menu)
#     # print(type(menu))
#     str1 = 'Colds'
#     str2 = 'Bubble Tea'
#     str3 = 'Tomato Salad'
#     str4 = 'Beer'
#     shop = obj.collection.find_one({'Menu': menu[0]})
#     # print('Shop :', shop)
#     # print(type(shop))
#     b = 0
#     g = 0
#     list1 = []
#     list2 = []
#     list5 = ''
#     # menu2 = obj.collection.find_one({'Shop Name': 'Barlala'})
#     # # print(menu2)
#     # menu3 = menu2.get('Menu')
#     # print(menu3)
#     for i in menu:
#         for j in i:
#             if j == str4:
#                 c = obj.collection.find_one({'Menu': i})
#                 d = c.get('Shop Name')
#                 print('Shop :', d)
#                 print(str4)
#                 b = i.get(str4)
#                 list1.append(d)
#                 list2.append(b)
#                 list3 = zip(list1, list2)
#                 list4 = dict(list3)
#                 print(list4)
#                 list5 = json.dumps(list4)
#                 print(list5)
#                 print(type(list5))
#                 print(json.loads(list5))
#                 print(type(json.loads(list5)))
#                 g = g + b
#                 break
#                 # print(i.get(str2))
#                 # break
#             else:
#                 list5 = 'none'
#         # break
#     return list5
#
#
# def total_cost(total_list, payment):
#     total = 0
#     menu_list = str()
#     for list_i in total_list:
#         menu_str = obj.check_menu(list_i[1])
#         menu_dict = json.loads(menu_str)
#         price = menu_dict.get(list_i[0])
#         cost = price * int(list_i[2])
#         total += cost
#         menu_list += list_i[2] + ' * ' + list_i[1] + '(' + str(price) + ') = ' + str(cost) + '\n'
#     deli_fee = 3000
#     total += deli_fee
#     deli_fee2 = 'Deli fees = ' + str(deli_fee) + '\n'
#     payment_type = 'Payment Type >> ' + payment + '\n'
#     menu = '......dailY deli......\n'
#     menu += menu_list + deli_fee2 + 'Total cost = ' + str(total) + '\n' + payment_type + '--- THANK YOU FOR ' \
#                                                                                          'SUPPORTING US! ---'
#     return menu
#
# def count_cost(shop, item, count):
#     menu_str = obj.check_menu(item)
#     menu_dict = json.loads(menu_str)
#     price = menu_dict.get(shop)
#     cost = item + "'s cost = " + str(price)
#     # count = '\n' + 'Count = ' + count
#     # total = '\n' + 'Total cost = ' + str(price * int(count))
#     # cost += count + total
#     return cost
#
#
# # def check_menu(item):
# #     menu = obj.collection.find().distinct('Menu')
# #     shop_list = []
# #     price_list = []
# #     count = 0
# #     menu_str = str()
# #     for i in menu:
# #         for j in i:
# #             if j == item:
# #                 menu_dict = obj.collection.find_one({'Menu': i})
# #                 shop_name = menu_dict.get('Shop Name')
# #                 price = i.get(item)
# #                 shop_list.append(shop_name)
# #                 price_list.append(price)
# #                 menu_list = zip(shop_list, price_list)
# #                 menu_str = json.dumps(dict(menu_list))
# #                 count += 1
# #             else:
# #                 count += 0
# #     if count > 0:
# #         return menu_str
# #     else:
# #         return 'none'
#
#
# if __name__ == '__main__':
#     print('Start.')
#     a = check()
#     if 'none' not in a:
#         print('Your item is available.')
#     else:
#         print('\nYour item is unavailable')
#         print('Price = ', a)
#         print(type(a))
#         list1 = [['Barlala', 'Beer', '5'], ['Lotteria', 'Pizza', '2'], ['Pan Ei', 'Tomato Salad', '3']]
#         str1 = total_cost(list1, 'Cash On Deli')
#         print(str1)
#         list2 = ['Barlala', 'Beer', '5']
#         str2 = count_cost(list2[0], list2[1], list2[2])
#         print(str2)
