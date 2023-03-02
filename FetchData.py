import pymongo


class DatabaseClass:
    def __init__(self, toSearchName):
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.database = self.connection["MyFirstDb"]
        self.collection = self.database["My_col1"]
        self.toSearchName = toSearchName

    def databaseMethod(self):
        toReturn = ''
        try:
            myQuery = {'name': self.toSearchName}
            data_1 = self.collection.find(myQuery)
            print("type", type(data_1))

            for z in data_1:

                if z['name'] == self.toSearchName:

                    findingData = self.collection.find(myQuery)
                    for i in findingData:
                        toReturn = i['Hobby']

            return toReturn

        except Exception as err:
            print(err)


if __name__ == "__main__":
    db = DatabaseClass('development')
    data = db.databaseMethod()
    print(data)
