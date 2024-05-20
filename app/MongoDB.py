
from pymongo import MongoClient
import time
# start_time = time.time()



# collection.drop()
# data = {
#     "_id": 2,
#     "User": {
#         "ID" : 12345,
#         "Referal_ID": None,
#         "Web": {
#             "WebName": "Shakal_crypto",
#             "Position_1": {
    #LongOrShortLongOrShortLongOrShortLongOrShort
#                 "TokenName": "BTC",
#                 "Money": 1000,
#                 "Leverage": 10,
#                 "StartPlace": "Market",
#                 "TakeProfit": 1200,
#                 "StopLoss": 950
#             },

            # "Position_2": {
            #     "TokenName": "QQQ",
            #     "Money": 1012300,
            #     "Leverage": 10,
            #     "StartPlace": "Market",
            #     "TakeProfit": 1200,
            #     "StopLoss": 950
            # },

            # "Position_3": {
            #     "TokenName": "RRRR",
            #     "Money": 152000,
            #     "Leverage": 10,
            #     "StartPlace": "Market",
            #     "TakeProfit": 1200,
            #     "StopLoss": 950
            # },

            # "Position_4": {
            #     "TokenName": "III",
            #     "Money": 102300,
            #     "Leverage": 10,
            #     "StartPlace": "Market",
            #     "TakeProfit": 1200,
            #     "StopLoss": 950
            # },

            # "Position_5": {
            #     "TokenName": "PPP",
            #     "Money": 10,
            #     "Leverage": 10,
            #     "StartPlace": "Market",
            #     "TakeProfit": 1200,
            #     "StopLoss": 950
            # },


#         }
#     }
# }

# collection.insert_one(data)




# user = collection.find_one({
#     "_id" : 2
# })


# print(user)



class Table:

    def __init__(self, dbase):
        cluster = MongoClient(dbase)
        db = cluster["admin"]
        self.collection = db["Collection_OpenDeal"]

    def Count_Data(self):
        count_users = self.collection.count_documents({})
        who_have_WebName = self.collection.count_documents({"User.Web.WebName": {"$exists": True, "$ne": None}})
        Data = [count_users, who_have_WebName]
        return Data


    def AddUser(self, UserId, referal_id=None):
        try:
            new_user = {
                "User": {
                    "ID": UserId,
                    "Referal_ID": referal_id,
                }
            }

            self.collection.insert_one(new_user)

        except Exception as error:
            print("Error AddUser", error)


    def CheckRegistr(self, UserId):
        try:
            result = self.collection.find_one({'User.ID': UserId})
            return bool(result)

        except Exception as error:
            print("Error CheckRegistr", error)


    def CheckOnSame_WebName(self, WebName):

        filter = {'User.Web.WebName': WebName}
        # projection = {'User.Web.WebName': 1}

        result = self.collection.find_one(filter) #['User']['Web']['WebName']
        print(bool(result))
        return bool(result)


    def Check_WebName(self, UserId):
        try:
            filter = {'User.ID': UserId, 'User.Web.WebName': {'$exists': True, '$ne': ''}}
            projection = {'_id': 0}
            result = self.collection.find_one(filter, projection)
            if result is not None:
                return result['User']['Web']['WebName']
            else:
                return False

        except Exception as error:
            print("Error Check_WebName", error)
            return "Another_Mistake000"



    def Add_WebName(self, WebName, UserId):
        try:
            user = self.Check_WebName(UserId)
            print(user)

            if user == False:
                self.collection.update_one({'User.ID': UserId}, {"$set": {"User.Web": {"WebName": WebName,
                "Position_1": {"TokenName": ""},
                "Position_2": {"TokenName": ""},
                "Position_3": {"TokenName": ""}}}})
                return True
                
            else:
                return "У вас уже есть канал!"



        except Exception as error:
            print("Error Add_WebName", error)




    def Add_Position(self, UserId, TokenName, Money, Leverage, StartPlace, Link_with_post, TakeProfit, StopLoss, LongOrShort):
        try:
            filter = {'User.ID': UserId}

            data = {
                "TokenName": TokenName,
                "Money": Money,
                "Leverage": Leverage,
                "StartPlace": StartPlace,
                "Link_with_post": Link_with_post,
                "TakeProfit": TakeProfit,
                "StopLoss": StopLoss,
                "LongOrShort": LongOrShort,
                "Fix_or_not": None
            }

            user = self.Check_WebName(UserId=UserId)
            print(user)
            if user != False:
                for i in range(1, 4):
                    projection = {f'User.Web.Position_{i}': 1}
                    Position_check = self.collection.find_one(filter, projection)['User']['Web'][f'Position_{i}']['TokenName']
                    if Position_check in "":
                        update = {"$set": {f"User.Web.Position_{i}": data}}
                        self.collection.update_one(filter, update)
                        print("Added position successfully")
                        return True  # Added position successfully
                    else:
                        if i == 3:
                            for i in range(1, 4):
                                projection = {f'User.Web.Position_{i}': 1}
                                fixed_position = self.collection.find_one(filter, projection)['User']['Web'][f'Position_{i}']['Fix_or_not']
                                if fixed_position == 1 or fixed_position == 0:
                                    update = {"$set": {f"User.Web.Position_{i}": data}}
                                    self.collection.update_one(filter, update)
                                    print("Added position successfully")
                                    return True  # Added position successfully
                                else:
                                    if i == 3:
                                        print("Все позиции активны! Удалите хотя бы одну позицию")
                                        return "All_Positions_full"

            else:
                print("У вас нету канала!")
                return False  # User not found

        except Exception as error:
            print("Add_Position error:", error)


    
    def Get_Positions(self, WebName):
        try:
            filter = {'User.Web.WebName': WebName}
            All_Positions = []
            for i in range(1, 4):
                projection = {f'User.Web.Position_{i}': 1}
                result = self.collection.find_one(filter, projection)['User']['Web']
                All_Positions.append(result)
            return All_Positions


        except Exception as error:
            print("Get_Positions", error)


    def Delete_Positions(self, UserId, Position_num):
        try:
            user = self.Check_WebName(UserId)
            print(user)

            if user:
                print(1111)
                self.collection.update_one(
                {'User.ID': UserId},
                {'$set': {f'User.Web.Position_{Position_num}':{"TokenName":""}}})
                #Нахуй web просто буду выводть инлайн кнопки с именами койнов

                return True
                
            else:
                return False
    
        except Exception as error:
            print("Delete_Positions", error)
          
          
    def Delete_Channel(self, UserId):
        try:
            user = self.Check_WebName(UserId)
            print(user)

            if user:
                self.collection.update_one(
                {'User.ID': UserId},
                {'$unset': {'User.Web': ''}})

                return True
                
            else:
                return False
    
        except Exception as error:
            print("Delete_Channel", error)


    #     except Exception as error:
    #         print("Error Add_WebName", error)


    def Event_for_Positions(self, WebName, TP_or_SL, Num_position):
        try:
            print(WebName, Num_position)
            self.collection.update_one(
                {'User.Web.WebName': WebName},
                {'$set': {f'User.Web.Position_{Num_position}.Fix_or_not': TP_or_SL}})
            print(8888)
        except Exception as error:
            print("Add_Position error:", error)

    # def Get_Event_for_Positions(self, UserId):
    #     try:
    #         list_with_data = []
    #         document = self.collection.find_one({"User.ID": UserId})
    #         if document:
    #             positions = document["User"]["Web"]
    #             for position in positions.values():
    #                 if "Fixed_position" in position:
    #                     fixed_position = position["Fixed_position"]
    #                     list_with_data.append[fixed_position]
    #                 else:
    #                     list_with_data.append[None]
    #         print(list_with_data)
    #         return list_with_data
                
    #     except Exception as error:
    #         print("Get_Positions", error)

    def Check_Event_for_Positions(self, WebName, Num_position):
        try:
            document = self.collection.find_one({'User.Web.WebName': WebName})
            if 'Fix_or_not' in document['User']['Web'][f'Position_{Num_position}'] != None:
                print(document['User']['Web'][f'Position_2']['Fix_or_not'])
                return document['User']['Web'][f'Position_{Num_position}']['Fix_or_not']
            else:
                print("Ошибка в Check_Event_for_Positions")
                return False

        except Exception as error:
            print("Get_Positions", error)


db = Table("mongodb://expin12267:.aRTTIG12267@217.28.220.129:36607/OpenDeal_DB?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.0")

# db.CheckRegistr(UserId="1qeq")

# db.Count_Data()

# a = db.Delete_Positions(777, 1)
# print(a)

# db.Get_Positions("GODUDE")

# db.AddUser(UserId=777)

# db.Add_WebName(UserId="6181334530", WebName="Example")  

# a = db.Check_Event_for_Positions(333, 1)
# print(a)

# a = db.Check_WebName(UserId=324430515)
# print(a)

# db.CheckOnSame_WebName(WebName="je75tjnwtry")

#db.Add_Position(UserId=6181334530, TokenName="ETHUSDT", Money="1000", Leverage=40, StartPlace=2,  TakeProfit="5700", StopLoss="1000", LongOrShort=1)
# print(a)
# WebName = "TONP"
# UserId = 333
# if not db.CheckOnSame_WebName(WebName):
#     db.Add_WebName(WebName = WebName, UserId = UserId)  6181334530



cluster = MongoClient("mongodb://expin12267:.aRTTIG12267@217.28.220.129:36607/OpenDeal_DB?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.0")
# 

# filter = {'User.ID': 333}
# data = {'TokenName': '','fixed_position': 1}
# update = {"$set": {f"User.Web.Position_{1}": data}}
# collection.update_one(filter, update)

# collection.update_one({'User.ID': 333}, {"$set": {"User.Web": {"WebName": "TONP",
#     "Position_1": {"TokenName": ""},
#     "Position_2": {"TokenName": ""},
#     "Position_3": {"TokenName": ""}}}})

# data = {
#     "TokenName": "BTCUSDT",
#     "Money": 10000,
#     "Leverage": 25,
#     "StartPlace": 30000,
#     "TakeProfit": 25000,
#     "StopLoss": 31000,
#     "LongOrShort": 0
# }

# query = {'User.ID': 789}
# update = {"$set": {f"User.Web.Position_2": data}}
# collection.update_one(query, update)
# print("Added position successfully")


db = cluster["OpenDeal_DB"]
collection = db["Collection_OpenDeal"]
#collection.drop({})

results = collection.find()
# end_time = time.time()
# execution_time = end_time - start_time

# print(f"Время выполнения: {execution_time} секунд")
for result in results:
    print(result)