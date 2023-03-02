# import pickle
#
# data = [{"_id": 1, "Shop Name": "Barlala", "Menu": "Beer, Colds, Juices, BBQ, Hotpot, Salads, Many Fried Snacks, "
#                                                    "Beverages"},
#         {"_id": 2, "Shop Name": "MayKantKaw", "Menu": "Tea Leaf Salad, Popcorn Salad, Ginger Salad, Pennyworth Salad, "
#                                                       "Tomato Salad"},
#         {"_id": 3, "Shop Name": "Thu Tasty", "Menu": "Lemon, Lime, Orange, Strawberry, Aml, Grape, Apple, Pineapple, "
#                                                      "Watermelon"},
#         {"_id": 4, "Shop Name": "Lotteria", "Menu": "Fried Chicken, Burger, Cola, fries, rice box"}]
# listToStr = ' '.join(map(str, data))
# # print(type(listToStr))
# # print(listToStr)
#
#
# dic = {"_id": 4, "Shop Name": "Lotteria", "Menu": "Fried Chicken, Burger, Cola, Fries, Rice Box"}
# # msg = pickle.dumps(dic)
# # red = pickle.loads(msg)
# # msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
# print(type(dic))
# print(dic)
# # print(msg)
# # print(type(msg))
# # print(red)
# # print(type(red))
# strg = str(dic)
# print(type(strg))
# print(strg)
#
# # phNo = int(input("Enter Your PhoneNumber :"))
# # name = input('Enter Your Username    :')
# # p_word = input('Enter Your Password    :')
# # c_pass = input('Confirm Your Password  :')
# # addr = input('Enter Your Address     :')
# # dic_c = {"Username": name, "Password": p_word, "PhoneNumber": phNo, "Address": addr}
# # c_str = str(dic_c)
# # print(dic_c)
# # print(type(dic_c))
# # print(c_str)
# # print(type(c_str))
# c_input = 'iEnter Your PhoneNumber :, Enter Your Name :, Enter Your Password :, Confirm Your Password :, ' \
#                   'Enter Your Address : '
# s_input = c_input.split(', ')
# print(type(s_input))
# print(s_input)
# for i in s_input:
#     print(i)
# list_to_str = '\n'.join(map(str, s_input))
# print(type(list_to_str))
# print(list_to_str)

from database import Deliver
lit = [959, 'aung', 'kaung', 'kaung', 'sett']
print(lit[2])
print(lit[3])
if lit[2] != lit[3]:
    print("same.")
else:
    print("different.")

obj = Deliver()
id_ = obj.collection_2.find().distinct("_id")
print(id_)
print("len :", len(id_))
i = len(id_)
print(type(i))
print("Last index :", id_[i-1])
for i in id_:
    print(i)

lit = ['959222222222', ' fi']
phNo = obj.collection_2.find().distinct('PhoneNumber')
print(phNo)
for i in phNo:
    print(i)
    if int(lit[0]) == i:
        print("same.")
    else:
        print('different')
