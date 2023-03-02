import pymongo

try:
    connection = pymongo.MongoClient("localhost", 27017)
    database = connection["Database"]
    collection = database["Collection"]
    print("Connected.")
except Exception as error:
    print(error)

data = [{"_id": 4, "name": "R.Araujo", "club": "FCBarcelona", "Nation": "Uruguay", "Age": 22},
        {"_id": 5, "name": "Pedri", "club": "FCBarcelona", "Nation": "Spain", "Age": 20},
        {"_id": 6, "name": "O.Dembele", "club": "FCBarcelona", "Nation": "France", "Age": 25},
        {"_id": 7, "name": "Raphinha", "club": "FCBarcelona", "Nation": "Brazil", "Age": 26},
        {"_id": 1, "name": "F.de jong", "club": "FCBarcelona", "Nation": "Netherlands", "Age": 24}]
query = 'name'

try:
    # collection.drop()
    # print("Data Inserted.")

    # collection.delete_many({})
    # collection.insert_many(data)
    print("Ok.")
    # print(data)
    name = collection.find().distinct('name')
    name_s = '\n'.join(map(str, name))
    print(name)
    print(name_s)

    # for i in data_2:
    #     print(i)

except Exception as error:
    print(error)
