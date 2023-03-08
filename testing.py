# # # str1 = 'Enter Your PhoneNumber :*Enter Your Username    :$Enter Your Password    :' \
# # #                   '$Confirm Your Password  :$Enter Your Address     :'
# # # list1 = str1.split('*')
# # # str2 = str()
# # # print(list1)
# # # print(list1[0] + 'l')
# # # del list1[0]
# # # print(list1)
# # # str2 = str2.join(list1)
# # # print(str2)
# # # list2 = str2.split('$')
# # # for i in list2:
# # #     print(i)
# # #
# # # a = 'HellO'
# # # b = 'hello'
# # # print(a.upper(), b.upper())
# # # if a == b:
# # #     print('same')
# # # if a.upper() == b.upper():
# # #     print('same same')
# # #
# # # print(a.capitalize(), b.capitalize())
# # # print(a, b)
# # # total_list = [['barlala', 'beer', '10'], ['loTTeria', 'PIZZA', '2'], ['Pan-Ei', 'Tomato Salad', '5']]
# # # print(total_list)
# # # print('\n')
# # # for list_a in total_list:
# # #     for b in range(len(list_a)):
# # #         if b == 0:
# # #             list_a[b] = list_a[b].upper()
# # #         else:
# # #             list_a[b] = list_a[b].capitalize()
# # # print(total_list)
# # # print('Length 1 :', len(total_list))
# # # str3 = '\n'.join(map(str, total_list))
# # # print('string :', str3)
# # # for i in range(len(total_list)):
# # #     total_list.pop(0)
# # # print(total_list)
# # # print(type(total_list))
# # # print('Length 2 :', len(total_list))
# # total_list = [['barlala', 'beer', '10'], ['loTTeria', 'PIZZA', '2'], ['Pan-Ei', 'Tomato Salad', '5']]
# # print(total_list)
# # drop_list = ['Pan-p', 'Tomato Salad', '5']
# # # length = len(total_list)
# # # for i in range(length):
# # #     print('a')
# # #     if total_list[i][1].title() == drop_list[0].title():
# # #         menu = int(total_list[i][2])
# # #         drop = int(drop_list[1])
# # #         menu -= drop
# # #         total_list[i][2] = str(menu)
# # #         if menu <= 0:
# # #             total_list.pop(i)
# # #             break
# # # print(total_list)
# # # lisst = []
# # # for list_o in total_list:
# # #     if list_o[0] == drop_list[0] and list_o[1] == drop_list[1]:
# # #         count1 = int(list_o[2])
# # #         count2 = int(drop_list[2])
# # #         count1 += count2
# # #         list_o[2] = str(count1)
# # #         print(list_o)
# # #     else:
# # #         total_list.append(drop_list)
# # # cancel = 'Order Cancelled!'
# # # cancel += '\nYour Menu Chart >> \n' + '\n'.join(map(str, total_list))
# # # print(cancel)
# #
# from database import Deliver
# # import datetime
#
# #
# obj = Deliver()
# #
# # order = ['barlala', 'tomato salad', '4']
# # menu = obj.collection.find().distinct('Menu')
# # for i in menu:
# #     for j in i:
# #         if j == order[1].title():
# #             whole_menu = obj.collection.find_one({'Menu': i})
# #             shop = whole_menu.get('Shop Name')
# #             print(whole_menu)
# #             print(shop)
# #             if shop == order[0].upper():
# #                 print('present')
# #                 break
# #             else:
# #                 print('absent')
# #
# # a = 959222222222
# # name = obj.collection_2.find().distinct('PhoneNumber')
# # print(name)
# # phNo = obj.collection_2.find_one({'PhoneNumber': a})
# # print(phNo)
# # obj.History.insert_one({
# #     '_id': 1,
# #     'firstName': "John",
# #     'lastName': "King",
# #     'email': "john.king@abc.com",
# #     'salary': 5000,
# #     'skills': ["Angular", "React", "MongoDB"]
# # })
# # var query = { $set: {'firstName':"Morgan"}}
# # obj.History.update_one({'_id': 1}, {'_id': 1, 'firstName': 'Morgan'})
# # phNo = 959123321123
# # obj.History.update_many({"PhoneNumber": 0}, {"$set": {"History": [{"PhoneNumber": phNo, "shop name": "lotteria"}]}})
#
# # x = datetime.datetime.now()
# # date = x.strftime("%d/%b/%Y__%I:%M:%S-%p")
# # print(date)
# # print(type(date))
# # a = '7'
# # print(ord(a))
# # print(type(ord(a)))
# #
# # phNo = '9596654456'
# # count = 0
# # for i in phNo:
# #     if 48 <= ord(i) <= 57:
# #         count += 1
# #     else:
# #         count = 0
# #         break
# # print('Count :', count, type(count))
# #
# # phNum = 959453741976
# # count = 0
# # phNumber = obj.collection_2.find().distinct('PhoneNumber')
# # for i in phNumber:
# #     if phNo == i:
# #         data = obj.collection_2.find_one({'PhoneNumber': phNo})
# #         sign_in = data.get('Sign-in')
# #         sign_list = sign_in.split('@')
# #         for j in sign_list:
# #             if j == 'sign-in':
# #                 count += 1
# # if count > 0:
# #     rec_data = obj.collection_2.find_one({'PhoneNumber': phNo})
# #     record = rec_data.get('Record')
# #     original_rec = {'Record': record}
# #     updated_rec = {'$set': {'Record': record + '@record'}}
# #     obj.collection_2.update_one(original_rec, updated_rec)
# #     print('Record updated.')
# # else:
# #     print('no record update.')
# # phNumber = obj.collection_2.find().distinct('PhoneNumber')
# # for i in phNumber:
# #     if phNum == i:
# #         data = obj.collection_2.find_one({'PhoneNumber': phNum})
# #         sign_in = data.get('Sign-in')
# #         original_rec = {'Sign-in': sign_in}
# #         updated_rec = {'$set': {'Sign-in': sign_in + 1}}
# #         obj.collection_2.update_one(original_rec, updated_rec)
# #         print('Sign-in updated.')
# list_total = [['LOTTERIA', 'Pizza', '5'], ['BARLALA', 'Beer', '10'], ['PAN-EI', 'Tea Leaf Salad', '2']]
# payment = 'Prepaid'
# phoneNo = 959966760561
# count_t = 0
# phoneNum = obj.collection_2.find().distinct('PhoneNumber')
# order_id = obj.History.find().distinct('_id')
# i = len(order_id)
# bill = obj.total_cost(list_total, payment, phoneNo)
# for i in phoneNum:
#     if phoneNo == i:
#         ph_doc = obj.collection_2.find_one({'PhoneNumber': phoneNo})
#         record = ph_doc.get('Record')
#         original_record = {'Record': record}
#         updated_record = {'$set': {'Record': record + '@\n\n' + bill}}
#         obj.collection_2.update_one(original_record, updated_record)
#         print('Sign-in record updated.')
#         count_t = 1
#         break
#     else:
#         count_t = 0
# if count_t == 0:
#     obj.History.insert_one({'_id': order_id[-1]+1, 'PhoneNumber': phoneNo, 'Order-History': bill})
#     print('No-sign-in record updated.')
