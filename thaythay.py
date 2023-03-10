# from database import Deliver
#
# obj = Deliver()
#
# menu_list = [['LOTTERIA', 'Pizza', '5']]
# pay_ment = 'Prepaid'
# cusPh = 959966760561
# location = '8'
# deli_bill = obj.total_cost(menu_list, pay_ment, cusPh, location)
# deli_doc = {}
# location = int(location)
# if location == 1 or location == 2:
#     deli_doc = obj.Deli_Men.find_one({'PhoneNumber': 959171717171})
# elif location == 3 or location == 4:
#     deli_doc = obj.Deli_Men.find_one({'PhoneNumber': 959272727272})
# elif location == 5 or location == 6:
#     deli_doc = obj.Deli_Men.find_one({'PhoneNumber': 959373737373})
# elif location == 7 or location == 8:
#     deli_doc = obj.Deli_Men.find_one({'PhoneNumber': 959474747474})
# elif location == 9 or location == 10:
#     deli_doc = obj.Deli_Men.find_one({'PhoneNumber': 959575757575})
# deli_req = deli_doc.get('Customer-Order')
# original_req = {'Customer-Order': deli_req}
# updated_req = {'$set': {'Customer-Order': deli_req + '@\n\n' + deli_bill}}
# obj.Deli_Men.update_one(original_req, updated_req)
# duty = deli_doc.get('Duty-Record')
# original_duty = {'Duty-Record': duty}
# updated_duty = {'$set': {'Duty-Record': duty + '@\nduty'}}
# obj.Deli_Men.update_one(original_duty, updated_duty)
# print('Deli-record updated.')
str1 = 'loop'
list1 = str1.split(',')
print(list1)
strS = ','.join(map(str, list1))
print(strS)
