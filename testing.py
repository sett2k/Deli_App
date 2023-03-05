# # str1 = 'Enter Your PhoneNumber :*Enter Your Username    :$Enter Your Password    :' \
# #                   '$Confirm Your Password  :$Enter Your Address     :'
# # list1 = str1.split('*')
# # str2 = str()
# # print(list1)
# # print(list1[0] + 'l')
# # del list1[0]
# # print(list1)
# # str2 = str2.join(list1)
# # print(str2)
# # list2 = str2.split('$')
# # for i in list2:
# #     print(i)
# #
# # a = 'HellO'
# # b = 'hello'
# # print(a.upper(), b.upper())
# # if a == b:
# #     print('same')
# # if a.upper() == b.upper():
# #     print('same same')
# #
# # print(a.capitalize(), b.capitalize())
# # print(a, b)
# # total_list = [['barlala', 'beer', '10'], ['loTTeria', 'PIZZA', '2'], ['Pan-Ei', 'Tomato Salad', '5']]
# # print(total_list)
# # print('\n')
# # for list_a in total_list:
# #     for b in range(len(list_a)):
# #         if b == 0:
# #             list_a[b] = list_a[b].upper()
# #         else:
# #             list_a[b] = list_a[b].capitalize()
# # print(total_list)
# # print('Length 1 :', len(total_list))
# # str3 = '\n'.join(map(str, total_list))
# # print('string :', str3)
# # for i in range(len(total_list)):
# #     total_list.pop(0)
# # print(total_list)
# # print(type(total_list))
# # print('Length 2 :', len(total_list))
# total_list = [['barlala', 'beer', '10'], ['loTTeria', 'PIZZA', '2'], ['Pan-Ei', 'Tomato Salad', '5']]
# print(total_list)
# drop_list = ['Pan-p', 'Tomato Salad', '5']
# # length = len(total_list)
# # for i in range(length):
# #     print('a')
# #     if total_list[i][1].title() == drop_list[0].title():
# #         menu = int(total_list[i][2])
# #         drop = int(drop_list[1])
# #         menu -= drop
# #         total_list[i][2] = str(menu)
# #         if menu <= 0:
# #             total_list.pop(i)
# #             break
# # print(total_list)
# # lisst = []
# # for list_o in total_list:
# #     if list_o[0] == drop_list[0] and list_o[1] == drop_list[1]:
# #         count1 = int(list_o[2])
# #         count2 = int(drop_list[2])
# #         count1 += count2
# #         list_o[2] = str(count1)
# #         print(list_o)
# #     else:
# #         total_list.append(drop_list)
# # cancel = 'Order Cancelled!'
# # cancel += '\nYour Menu Chart >> \n' + '\n'.join(map(str, total_list))
# # print(cancel)
#
from database import Deliver
#
obj = Deliver()
#
# order = ['barlala', 'tomato salad', '4']
# menu = obj.collection.find().distinct('Menu')
# for i in menu:
#     for j in i:
#         if j == order[1].title():
#             whole_menu = obj.collection.find_one({'Menu': i})
#             shop = whole_menu.get('Shop Name')
#             print(whole_menu)
#             print(shop)
#             if shop == order[0].upper():
#                 print('present')
#                 break
#             else:
#                 print('absent')
#
name = obj.collection_2.find().distinct('PhoneNumber')
print(name)
h = obj.collection_2.find_one({'PhoneNumber': name[0]})
print(h)
i = h.get('Sign-in')
print(i)
i += 1
print(i)
print(h)
