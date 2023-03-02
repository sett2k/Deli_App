import json

from database import Deliver

obj = Deliver()
# strg = 'afoasidfk'
# print(len(strg))
# print(strg)
#
# phNo = 959111222333
# pass_p = obj.collection_2.find_one({'PhoneNumber': phNo})
# print(pass_p)
# a = pass_p.get('Password')
# print(a)
# print(type(a))
# print('\n\n')

# menu = obj.collection.find({}, {'_id': 0, 'Shop Name': 1, 'Menu': 1})
# rec = obj.collection.find({}, {'_id': 0, 'Shop Name': 1, 'Menu': 1})
# men = '\n'.join(map(str, menu))
# print(menu)
# print(type(menu))
# print(men)
# print(type(men))

# menu = obj.collection.find().distinct('Shop Name')
# menu_s = '", "'.join(map(str, menu))
# menu_l = menu_s.split('", "')
# print(menu_l)
# print(menu_l[1])
# print(type(menu_l[1]))
# # print('Food Stores >> "' + menu_s + '"')
# send_str = 'Food Stores >> "' + menu_s + '"'
# for i in menu_l:
#     menu1 = obj.collection.find_one({'Shop Name': i})
#     shop = i + ' - ' + menu1.get('Menu')
#     send_str = send_str + '\n' + shop
#     # print(shop)
# print(send_str)
# print(type(send_str))
#
# _id = obj.collection_2.find().distinct('_id')
# print(_id)
# i = len(_id)
# print(_id[i - 1])

m_dict = {"_id": 1, "Shop Name": "Barlala", "Menu": {"Beer": 2000, 'Colds': 1500, 'Juices': 1500, 'BBQ': 10000,
                                                     'Hotpot': 8000, 'Salads': 2000, 'Fried Snacks': 2500,
                                                     'Beverages': 2000}}
s_dict = obj.collection.find_one({'Shop Name': 'Barlala'})
m_m = s_dict.get('Menu')
m_s = str()
for key in m_m:
    m_s += key + ' - ' + str(m_m[key]) + ',\n'
ml = m_s.split(',\n')
print(m_m)
print(type(m_m))
print(m_s)
print(type(m_s))
print(ml)
print(type(ml))

a = 'lafjdsijk'
b = json.loads(a)
print(b)
