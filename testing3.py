import json

from database import Deliver

obj = Deliver()


def check():
    menu = obj.collection.find().distinct('Menu')
    # print(menu)
    # print(type(menu))
    str1 = 'Colds'
    str2 = 'Bubble Tea'
    str3 = 'Tomato Salad'
    str4 = 'Beer'
    shop = obj.collection.find_one({'Menu': menu[0]})
    # print('Shop :', shop)
    # print(type(shop))
    b = 0
    g = 0
    list1 = []
    list2 = []
    list5 = ''
    # menu2 = obj.collection.find_one({'Shop Name': 'Barlala'})
    # # print(menu2)
    # menu3 = menu2.get('Menu')
    # print(menu3)
    for i in menu:
        for j in i:
            if j == str4:
                c = obj.collection.find_one({'Menu': i})
                d = c.get('Shop Name')
                print('Shop :', d)
                print(str4)
                b = i.get(str4)
                list1.append(d)
                list2.append(b)
                list3 = zip(list1, list2)
                list4 = dict(list3)
                print(list4)
                list5 = json.dumps(list4)
                print(list5)
                print(type(list5))
                print(json.loads(list5))
                print(type(json.loads(list5)))
                g = g + b
                break
                # print(i.get(str2))
                # break
            else:
                list5 = 'none'
        # break
    return list5


if __name__ == '__main__':
    print('Start.')
    a = check()
    if 'none' not in a:
        print('Your item is available.')
    else:
        print('\nYour item is unavailable')
        print('Price = ', a)
        print(type(a))
