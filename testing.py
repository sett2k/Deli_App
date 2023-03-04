# str1 = 'Enter Your PhoneNumber :*Enter Your Username    :$Enter Your Password    :' \
#                   '$Confirm Your Password  :$Enter Your Address     :'
# list1 = str1.split('*')
# str2 = str()
# print(list1)
# print(list1[0] + 'l')
# del list1[0]
# print(list1)
# str2 = str2.join(list1)
# print(str2)
# list2 = str2.split('$')
# for i in list2:
#     print(i)
#
# a = 'HellO'
# b = 'hello'
# print(a.upper(), b.upper())
# if a == b:
#     print('same')
# if a.upper() == b.upper():
#     print('same same')
#
# print(a.capitalize(), b.capitalize())
# print(a, b)
# total_list = [['barlala', 'beer', '10'], ['loTTeria', 'PIZZA', '2'], ['Pan-Ei', 'Tomato Salad', '5']]
# print(total_list)
# print('\n')
# for list_a in total_list:
#     for b in range(len(list_a)):
#         if b == 0:
#             list_a[b] = list_a[b].upper()
#         else:
#             list_a[b] = list_a[b].capitalize()
# print(total_list)
# print('Length 1 :', len(total_list))
# str3 = '\n'.join(map(str, total_list))
# print('string :', str3)
# for i in range(len(total_list)):
#     total_list.pop(0)
# print(total_list)
# print(type(total_list))
# print('Length 2 :', len(total_list))
total_list = [['barlala', 'beer', '10'], ['loTTeria', 'PIZZA', '2'], ['Pan-Ei', 'Tomato Salad', '5']]
print(total_list)
drop_list = ['Tomato Salad', '5']
# length = len(total_list)
# for i in range(length):
#     print('a')
#     if total_list[i][1].title() == drop_list[0].title():
#         menu = int(total_list[i][2])
#         drop = int(drop_list[1])
#         menu -= drop
#         total_list[i][2] = str(menu)
#         if menu <= 0:
#             total_list.pop(i)
#             break
print(total_list)
