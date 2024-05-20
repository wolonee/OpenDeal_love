
from re import A
import requests
import Data
import hmac
import hashlib
import time
from pybit.unified_trading import HTTP
import math

# def get_position_info():
#     url="https://api.bybit.com/v5/position/list"
#     curent_time = int(time.time() * 1000)


# # session = spot.HTTP(
# #     endpoint="https://api.bybit.com/v5/position/list",
# #     testnet=True,
# #     api_key="Rv3gmU0tBhzAp71OUm",
# #     api_secret="W9tAjQoVpgAZi6crQThGYDQyszCWD4eSDSzr",
# #     log_requests=True,
# # )

# # print(session.get_positions(
# #     category="linear",
# #     symbol="BTCUSD",
# # ))


# def get_mark_price_kline(coin):
#     url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={coin}&interval=1&limit=1"

#     payload={}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload)

#     print(response.text)

# mydict = {

#     "TokenName":[],
#     "Money":[],
#     "Shoulder":[],
#     "StartPlace":[],

#     }

# data_for_BossChannel = "BTCUSDT 2500 20 30200"
# main_data = list(data_for_BossChannel)

# a = "TokenName"
# # Money = "Money"
# # Shoulder = "Shoulder"
# # StartPlace = "StartPlace"

# num = 0

# PlacesList = ["Money", "Shoulder", "StartPlace"]

# for i in main_data:
#     if i != " ":
#         mydict[a].append(i)
#     else:
#         a = PlacesList[num]
#         num += 1
            
# AllPlacesList = ["TokenName", "Money", "Shoulder", "StartPlace"]

# TokenName = ''.join(mydict["TokenName"])
# Money = ''.join(mydict["Money"])
# Shoulder = ''.join(mydict["Shoulder"])
# StartPlace = ''.join(mydict["StartPlace"])

# a = '{"retCode":0,"retMsg":"OK","result":{"symbol":"BTCUSDT","category":"linear","list":[["1691995260000","29420","29420","29419.9","29419.9"]]}\n,"retExtInfo":{},"time":1691995306304}\n'}
# print(a.json().get("list")[0][2])
# num = int(float(101.49263880860903))
# a = "{:.1%}".format("{0.}{num}")
# OnlineCost = 19
# Money=600
# Shoulder=1
# StartPlace=16
# LongOrShort=1

# #1. Формулы для расчета прибыли и потери в процентах:
# #Прибыль (%) = ((Цена продажи - Цена покупки) / Цена покупки)  100
# #Потеря (%) = ((Цена покупки - Цена продажи) / Цена покупки)  100


# result_money = int(Money) * int(Shoulder)
# procent_for_main = round(float((int(float(OnlineCost)) - StartPlace)/StartPlace), 4)
# # total_cost = round(float((result_money * procent_for_main) + result_money), 3)
# total_procent = round(float((((int(float(OnlineCost)) - StartPlace)/StartPlace) * 100) * Shoulder), 2)
# main_profit = round(float(result_money * procent_for_main), 3)

# if LongOrShort == 1:
#     if total_procent >= 0:
#         print(f"+{main_profit}(+{total_procent}%)")
#     else:
#         print(f"{main_profit}({total_procent}%)")
# else:
#     total_procent = total_procent * -1
#     main_profit = main_profit * -1
#     if total_procent >= 0:
#         print(f"+{main_profit}(+{total_procent}%)")
#     else:
#         print(f"{main_profit}({total_procent}%)")
# sum_Anya = 50000
# Anya = 50000
# year = 0
# all_sum = 20000
# mouth = 1
# num = 30000
# for i in range(121):
#     if i < 1:
#         i += 1
#     else:
#         print(f"месяц - {mouth} сумма взноса - {num}")
#         mouth += 1
#         num += 1000
#         all_sum = num + all_sum
#         if i % 12 == 0:
#             year += 1
#             print(f"------------- Вклад 5% --------------\n       Прошел -- {year} -- год\n        Общая сумма - {all_sum}")
#             real_cost_with_cia = all_sum * 0.93
#             real_cost_with_vklad = all_sum * 0.98
#             num = num * 1.05
#             cia = all_sum 
#             enough_for = all_sum // 50000
#             print(f"----- Этого хватит на {enough_for} платежа -----\nбез вклада - {real_cost_with_cia}\nСо вкладом - {real_cost_with_vklad}")
#         else:
#             pass


# a = input("dw")
# mydict["Money"] = a


# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# user = 111
# if user == "TypeError000" or user == "KeyError000" or user == "Another_Mistake000":
#     if user == "TypeError000":
#         print("Нет такого юзера, нажмите start")
#     elif user == "KeyError000":
#         print("Вы не создали канал")
#     else:
#         print("Ошибка")
# else:
#     print("Da")


# a = [{'Position_1': {'TokenName': 'aaa', "NNNN" : 1},  'Position_2': {'TokenName': ''}, 'Position_3': {'TokenName': 'ddd'}, 'Position_4': {'TokenName': 'fff'}, 'Position_5': {'TokenName': ''}}]
# b = a[0]
# b = b['Position_1']
# print(b["TokenName"])
# for i in range(6):
#     if i == 0:
#         pass
#     else:
#         Have_not = b[f'Position_{i}']['TokenName']
#         if Have_not == '':
#             pass
#         else:
#             print(b[f'Position_{i}'])


# TokenName1   Leverage1   StartPlace1   LongOrShort1   TakeProfit1   StopLoss1   Money1


# MarkPrice0  total_procent0   main_profit0       OpenDeal/User_Channel
# start_time = time.time()

# for i in range(1):
#     StopLoss = 0.0007153
#     TakeProfit = 0.0007160
#     TokenName="1000PEPEUSDT"

#     url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={TokenName}&interval=1&limit=1"

#     payload={}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload)
#     OnlineCost = f'{response.json().get("result").get("list")[0][2]}'
#     OnlineCost = round(float(OnlineCost), 20)
    
#     # Add_Position
#     if TakeProfit <= StopLoss: #long
#         print("Take Profit can't be more than StopLoss! (LONG)")

#     if TakeProfit >= StopLoss: #short
#         print("Take Profit can't be less than StopLoss! (SHORT)")

#     #OnlineCost
#     #if long
#     if OnlineCost >= TakeProfit:
#         print("TakeProfit fixed! (green)") #if long

#     if OnlineCost <= StopLoss:
#         print("StopLoss fixed! (red)")

#     if OnlineCost <= TakeProfit:
#         print("TakeProfit fixed! (green)") #if short

#     # response = requests.request("GET", url, headers=headers, data=payload)

#     # OnlineCost = f'{response.json().get("result")}'

#     if OnlineCost != "{}":
#         print(OnlineCost)
#     else:
#         print("Такого токена нет")


# end_time = time.time()
# execution_time = end_time - start_time

# print(f"Время выполнения: {execution_time} секунд")
# for i in range(4):
#     a =1 
#     if a:
#         if a == 1:
#             a = 2
#         else:
#             a = 2
#     print(a)
# last_list = {"TokenName":[]}
# for i in range(4):
#     a = f"adfewfewaa{i}"
#     last_list["TokenName"].append(a)
# print(last_list["TokenName"][1])
# a = "klfwek,f"
# if a == True:
#     print(a)

# a = [{'Position_1': {'TokenName': ''}}, {'Position_2': {'TokenName': ''}}, {'Position_3': {'TokenName': ''}}]
# for item in a:
#     print(item)

# print(item)

# value = [{'Position_1': {'TokenName': 'TONUSDT', 'Money': 1000, 'Leverage': 20, 'StartPlace': 2.0, 'TakeProfit': 3, 'StopLoss': 1, 'LongOrShort': 1}}, {'Position_2': {'TokenName': 'JDDJJ'}}, {'Position_3': {'TokenName': 'OOOOO'}}]

# # a = value[0]['Position_1']
# # token_name = a['TokenName']
# # print(token_name)
# for i in range(1, 4):
#     num_for_value = i - 1
#     a = value[num_for_value][f'Position_{i}']
#     token_name = a['TokenName']

#     print(token_name)

# last_list = {'TokenName': ['TONUSDT'], 'LongOrShort': ['Long'], 'Leverage': [20], 'StartPlace': [2.0], 'MarkPrice': [2.0998], 'Procent': ['+99.8%'], 'StopLoss': [1], 'TakeProfit': [3]}

# if last_list['TokenName'][0]:
#     print(last_list['TokenName'][0])

# a = input("mfmief:")
# StartPlace = float(a)
# print(StartPlace)

# if 1 == 1:
#     if 1 != 1:
#         print("TakeProfit fixed! (green)") #if long
# print(2)


# last_list = {"TokenName":[]}
# a = 0
# for i in range(1, 4):
#     a += 1
#     if a != 1:
#         print(1)
# else:
#     print(2)
# print(last_list)

# a = """
# {% extends 'Main.html' %}

# {% if NonePositions %}
#   {{ NonePositions }}
# {% endif %}


# {% block conteiner_1 %}
#   {% if last_list['TokenName'][0] %}
#     {% if last_list['Fix_or_not'][0] == 1 %}
#     <div class="conteiner_1" style="background-color: rgba(32, 178, 108, 0.5); box-shadow: 0px 0px 30px 30px rgba(32, 178, 108, 0.5);">
#       <p class="font_LEMON_MILK" style="position: absolute; margin-top: 75px; font-size: 4vw;">Take Profit!</p>
#       <div class="all_token_info" style="opacity: 0.4;">
#     {% elif last_list['Fix_or_not'][0] == 0 %}
#     <div class="conteiner_1" style="background-color: rgba(239, 69, 74, 0.5); box-shadow: 0px 0px 30px 30px rgba(239, 69, 74, 0.5);">
#       <p class="font_LEMON_MILK" style="position: absolute; margin-top: 75px; font-size: 4vw;">Stop Loss!</p>
#       <div class="all_token_info" style="opacity: 0.4;">
#     {% else %}
#     <div class="conteiner_1"">
#       <div class="all_token_info">
#     {% endif %}
#         <div class="all_start_position_info">
#           <div class="token_position_Leverage">
#             <div class="token_and_position">
#               <div class="font_LEMON_MILK" style="font-size: 4vw;"> {{ last_list['TokenName'][0] }} </div>     <!-- TOKEN NAME -->
#               {% if last_list['LongOrShort'][0] == "Long" %}
#                 <div class="font_LEMON_MILK_LongShort" style="background-color: #20b26c; color: #fff;"> {{ last_list['LongOrShort'][0] }} </div> 
#               {% else %}
#                 <div class="font_LEMON_MILK_LongShort" style="background-color: #ef454a; color: #fff;"> {{ last_list['LongOrShort'][0] }} </div>
#               {% endif %}     <!-- LONG or SHORT -->
#             </div>
#             <div class="Leverage">
#               <div class="font_size_LEMON_MILK">Cross {{ last_list['Leverage'][0] }}x</div>  <!-- Leverage -->
#             </div>
#           </div>


#           <div class="start_and_mark">

#             <div class="start_price">
#               <div class="font_size_LEMON_MILK"> Start Place </div>   
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK"> {{ last_list['StartPlace'][0] }} </div>     <!-- START PLACE -->
#             </div>

#             <div class="mark_price">
#               <div class="font_size_LEMON_MILK"> Mark Price </div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK"> {{ last_list['MarkPrice'][0] }} </div>     <!-- MARK PRICE -->
#             </div>
#           </div>
#         </div>

#         <div class="result_info">

#           <div class="procent">
#           {% if last_list['Procent'][0] != None %}
#             {% if last_list['Procent'][0] >= 0 %}
#               <div class="font_LEMON_MILK" style="font-size: 4vw; color: #20b26c;">{{ last_list['Procent'][0] }}</div>
#             {% else %}
#               <div class="font_LEMON_MILK" style="font-size: 4vw; color: #ef454a;">{{ last_list['Procent'][0] }}</div>
#             {% endif %}     <!-- LONG or SHORT -->
#           {% else %}
#             <div class="font_LEMON_MILK" style="font-size: 4vw;">{{ last_list['Procent'][0] }}</div>
#           {% endif %}
#           </div>

#           <div class="end_positions">
#             <div class="stop_loss">
#               <div class="font_size_LEMON_MILK">Stop Loss</div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK" style="color: #ef454a;">{{ last_list['StopLoss'][0] }}</div>
#             </div>
#             <div class="take_profit">
#               <div class="font_size_LEMON_MILK">Take Profit</div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK" style="color: #20b26c;">{{ last_list['TakeProfit'][0] }}</div>
#             </div>
#           </div>
#         </div>
#       </div>
#     </div>
#   {% endif %}
# {% endblock %}

# {% block conteiner_2 %}
#   {% if last_list['TokenName'][1] %}
#     {% if last_list['Fix_or_not'][1] == 1 %}
#     <div class="conteiner_2" style="background-color: rgba(32, 178, 108, 0.5); box-shadow: 0px 0px 30px 30px rgba(32, 178, 108, 0.5);">
#       <p class="font_LEMON_MILK" style="position: absolute; margin-top: 75px; font-size: 4vw;">Take Profit!</p>
#       <div class="all_token_info" style="opacity: 0.4;">
#     {% elif last_list['Fix_or_not'][1] == 0 %}
#     <div class="conteiner_2" style="background-color: rgba(239, 69, 74, 0.5); box-shadow: 0px 0px 30px 30px rgba(239, 69, 74, 0.5);">
#       <p class="font_LEMON_MILK" style="position: absolute; margin-top: 75px; font-size: 4vw;">Stop Loss!</p>
#       <div class="all_token_info" style="opacity: 0.4;">
#     {% else %}
#     <div class="conteiner_2">
#       <div class="all_token_info">
#     {% endif %}
#         <div class="all_start_position_info">
#           <div class="token_position_Leverage">
#             <div class="token_and_position">
#               <div class="font_LEMON_MILK" style="font-size: 4vw;"> {{ last_list['TokenName'][1] }} </div>     <!-- TOKEN NAME -->
#               {% if last_list['LongOrShort'][1] == "Long" %}
#                 <div class="font_LEMON_MILK_LongShort" style="background-color: #20b26c; color: #fff;"> {{ last_list['LongOrShort'][0] }} </div> 
#               {% else %}
#                 <div class="font_LEMON_MILK_LongShort" style="background-color: #ef454a; color: #fff;"> {{ last_list['LongOrShort'][0] }} </div>
#               {% endif %}     <!-- LONG or SHORT -->
#             </div>
#             <div class="Leverage">
#               <div class="font_size_LEMON_MILK">Cross {{ last_list['Leverage'][1] }}x</div>  <!-- Leverage -->
#             </div>
#           </div>


#           <div class="start_and_mark">

#             <div class="start_price">
#               <div class="font_size_LEMON_MILK"> Start Place </div>   
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK"> {{ last_list['StartPlace'][1] }} </div>     <!-- START PLACE -->
#             </div>

#             <div class="mark_price">
#               <div class="font_size_LEMON_MILK"> Mark Price </div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK"> {{ last_list['MarkPrice'][1] }} </div>     <!-- MARK PRICE -->
#             </div>
#           </div>
#         </div>

#         <div class="result_info">

#           <div class="procent">
#           {% if last_list['Procent'][1] != None %}
#             {% if last_list['Procent'][1] >= 0 %}
#               <div class="font_LEMON_MILK" style="font-size: 4vw; color: #20b26c;">{{ last_list['Procent'][1] }}</div>
#             {% else %}
#               <div class="font_LEMON_MILK" style="font-size: 4vw; color: #ef454a;">{{ last_list['Procent'][1] }}</div>
#             {% endif %}     <!-- LONG or SHORT -->
#           {% else %}
#             <div class="font_LEMON_MILK" style="font-size: 4vw;">{{ last_list['Procent'][1] }}</div>
#           {% endif %}
#           </div>

#           <div class="end_positions">
#             <div class="stop_loss">
#               <div class="font_size_LEMON_MILK">Stop Loss</div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK" style="color: #ef454a;">{{ last_list['StopLoss'][1] }}</div>
#             </div>
#             <div class="take_profit">
#               <div class="font_size_LEMON_MILK">Take Profit</div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK" style="color: #20b26c;">{{ last_list['TakeProfit'][1] }}</div>
#             </div>
#           </div>
#         </div>
#       </div>
#     </div>
#   {% endif %}
# {% endblock %}

# {% block conteiner_3 %}
#   {% if last_list['TokenName'][2] %}
#     {% if last_list['Fix_or_not'][2] == 0 %}
#     <div class="conteiner_3" style="background-color: rgba(32, 178, 108, 0.5); box-shadow: 0px 0px 30px 30px rgba(32, 178, 108, 0.5);">
#       <p class="font_LEMON_MILK" style="position: absolute; margin-top: 75px; font-size: 4vw;">Take Profit!</p>
#       <div class="all_token_info" style="opacity: 0.4;">
#     {% elif last_list['Fix_or_not'][2] == 1 %}
#     <div class="conteiner_3" style="background-color: rgba(239, 69, 74, 0.5); box-shadow: 0px 0px 30px 30px rgba(239, 69, 74, 0.5);">
#       <p class="font_LEMON_MILK" style="position: absolute; margin-top: 75px; font-size: 4vw;">Stop Loss!</p>
#       <div class="all_token_info" style="opacity: 0.4;">
#     {% else %}
#     <div class="conteiner_3"">
#       <div class="all_token_info">
#     {% endif %}
#         <div class="all_start_position_info">
#           <div class="token_position_Leverage">
#             <div class="token_and_position">
#               <div class="font_LEMON_MILK" style="font-size: 4vw;"> {{ last_list['TokenName'][2] }} </div>     <!-- TOKEN NAME -->
#               {% if last_list['LongOrShort'][2] == "Long" %}
#                 <div class="font_LEMON_MILK_LongShort" style="background-color: #20b26c; color: #fff;"> {{ last_list['LongOrShort'][0] }} </div> 
#               {% else %}
#                 <div class="font_LEMON_MILK_LongShort" style="background-color: #ef454a; color: #fff;"> {{ last_list['LongOrShort'][0] }} </div>
#               {% endif %}     <!-- LONG or SHORT -->
#             </div>
#             <div class="Leverage">
#               <div class="font_size_LEMON_MILK">Cross {{ last_list['Leverage'][2] }}x</div>  <!-- Leverage -->
#             </div>
#           </div>


#           <div class="start_and_mark">

#             <div class="start_price">
#               <div class="font_size_LEMON_MILK"> Start Place </div>   
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK"> {{ last_list['StartPlace'][2] }} </div>     <!-- START PLACE -->
#             </div>

#             <div class="mark_price">
#               <div class="font_size_LEMON_MILK"> Mark Price </div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK"> {{ last_list['MarkPrice'][2] }} </div>     <!-- MARK PRICE -->
#             </div>
#           </div>
#         </div>

#         <div class="result_info">

#           <div class="procent">
#           {% if last_list['Procent'][2] != None %}
#             {% if last_list['Procent'][2] >= 0 %}
#               <div class="font_LEMON_MILK" style="font-size: 4vw; color: #20b26c;">{{ last_list['Procent'][2] }}</div>
#             {% else %}
#               <div class="font_LEMON_MILK" style="font-size: 4vw; color: #ef454a;">{{ last_list['Procent'][2] }}</div>
#             {% endif %}     <!-- LONG or SHORT -->
#           {% else %}
#             <div class="font_LEMON_MILK" style="font-size: 4vw;">{{ last_list['Procent'][2] }}</div>
#           {% endif %}
#           </div>

#           <div class="end_positions">
#             <div class="stop_loss">
#               <div class="font_size_LEMON_MILK">Stop Loss</div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK" style="color: #ef454a;">{{ last_list['StopLoss'][2] }}</div>
#             </div>
#             <div class="take_profit">
#               <div class="font_size_LEMON_MILK">Take Profit</div>
#               <div class="mini-border"></div>
#               <div class="num_size_LEMON_MILK" style="color: #20b26c;">{{ last_list['TakeProfit'][2] }}</div>
#             </div>
#           </div>
#         </div>
#       </div>
#     </div>
#   {% endif %}
# {% endblock %}
# """
# print(a)

# a = input("тцаузштзшацутамшцкитг:")
# a = str(a)
# w = int(float(a))
# print(w)

# a = None
# if a != None:
#     print(1)

# value = [{'Position_1': {'TokenName': 'TONUSDT', 'Money': 1000, 'Leverage': 10, 'StartPlace': 2.0, 'TakeProfit': 3.0, 'StopLoss': 1.0, 'LongOrShort': 1, 'fixed_position': None}}, {'Position_2': {'TokenName': 'BTCUSDT', 'Money': 2500, 'Leverage': 14, 'StartPlace': 30000.0, 'TakeProfit': 31000.0, 'StopLoss': 29000.0, 'LongOrShort': 1, 'fixed_position': 1}}, {'Position_3': {'TokenName': ''}}]
# for i in range(1, 4):
#     num_for_value = i - 1
#     Have_not = value[num_for_value][f'Position_{i}']['TokenName']
#     print(Have_not)

# from pymongo import MongoClient

# cluster = MongoClient("mongodb://expin12267:.aRTTIG12267@217.28.220.129:36607/OpenDeal_DB?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.0")
# db = cluster["OpenDeal_DB"]
# collection = db["Collection_OpenDeal"]

# WebName = "GODUDE"
# filter = {'User.Web.WebName': WebName}
# All_Positions = []
# for i in range(1, 4):
#     projection = {f'User.Web.Position_{i}': 1}
#     result = collection.find_one(filter, projection)['User']['Web']
#     All_Positions.append(result)
# print(All_Positions)


    # All_Positions = db.Get_Positions(WebName)
    # last_list = {"TokenName":[],
    #             "LongOrShort":[],
    #             "Leverage":[],
    #             "StartPlace":[],
    #             "MarkPrice":[],
    #             "Procent":[],
    #             "StopLoss":[],
    #             "TakeProfit":[],
    #             "Fix_or_not":[]
    #             }

    # NonePos = 0
    # for i in range(1, 4):
    #     num_for_value = i - 1
    #     Have_not = All_Positions[num_for_value][f'Position_{i}']['TokenName']
    #     if Have_not == None or Have_not == '':
    #         NonePos += 1
    #         if NonePos == 3:
    #             return render_template(f'user_{WebName}.html', NonePositions="Did not add positions", last_list=last_list)
    #     else:
    #         res = db.Check_Event_for_Positions(WebName=WebName, Num_position=i)
            
    #         num_i = All_Positions[num_for_value][f'Position_{i}']
    #         TokenName = num_i['TokenName']
    #         LongOrShort=num_i['LongOrShort']
    #         Leverage=num_i['Leverage']
    #         StartPlace=num_i['StartPlace']
    #         StopLoss=num_i['StopLoss']
    #         TakeProfit=num_i['TakeProfit']
    #         Money=num_i['Money']

    #         if res != None:
    #             last_list["TokenName"].append(TokenName)
    #             if LongOrShort == 1:
    #                 LongOrShort = "Long"
    #             else:
    #                 LongOrShort = "Short"
    #             last_list["LongOrShort"].append(LongOrShort)
    #             last_list["Leverage"].append(Leverage)
    #             last_list["StartPlace"].append(StartPlace)
    #             last_list["MarkPrice"].append(None)
    #             last_list["Procent"].append(None)
    #             last_list["StopLoss"].append(StopLoss)
    #             last_list["TakeProfit"].append(TakeProfit)
    #             last_list["Fix_or_not"].append(res)
            
    #         else:

    #             url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={TokenName}&interval=1&limit=1"

    #             payload={}
    #             headers = {}

    #             response = requests.request("GET", url, headers=headers, data=payload)
    #             OnlineCost = f'{response.json().get("result").get("list")[0][2]}'
    #             OnlineCost = round(float(OnlineCost), 20)
                
    #             ###########################     FIXED     ############################


    #             if LongOrShort == 1:
    #                 if OnlineCost >= float(TakeProfit):
    #                     db.Event_for_Positions(WebName=WebName, TP_or_SL=1, Num_position=i)

    #                 elif OnlineCost <= float(StopLoss):
    #                     db.Event_for_Positions(WebName=WebName, TP_or_SL=0, Num_position=i)

    #             if LongOrShort == 0:
    #                 if OnlineCost <= float(TakeProfit):
    #                     db.Event_for_Positions(WebName=WebName, TP_or_SL=1, Num_position=i)
                    
    #                 elif OnlineCost >= float(StopLoss):
    #                     db.Event_for_Positions(WebName=WebName, TP_or_SL=0, Num_position=i)

    #             ############################     END     #############################


    #             if Money != None:
    #                 Money = int(Money)
    #                 result_money = int(Money) * int(Leverage)
    #                 procent_for_main = round(float((OnlineCost - StartPlace)/StartPlace), 4)
    #                 # total_cost = round(float((result_money * procent_for_main) + result_money), 3)
    #                 total_procent = round(float((((OnlineCost - StartPlace)/StartPlace) * 100) * Leverage), 2)
    #                 main_profit = round(float(result_money * procent_for_main), 3)

    #                 if LongOrShort == 1:
    #                     LongOrShort = "Long"
    #                     if total_procent >= 0:
    #                         print(f"+{main_profit}(+{total_procent}%)")
    #                     else:
    #                         print(f"{main_profit}({total_procent}%)")

    #                 else:
    #                     total_procent = total_procent * - 1
    #                     main_profit = main_profit * - 1
    #                     LongOrShort = "Short"
    #                     if total_procent >= 0:
    #                         print(f"+{main_profit}(+{total_procent}%)")
                            
    #                     else:
    #                         print(f"{main_profit}({total_procent}%)")


    #         ###############################    Без MONEY Только Procent  #####################################

    #             else:
    #                 procent_for_main = round(float((OnlineCost - StartPlace)/StartPlace), 4)
    #                 # total_cost = round(float((result_money * procent_for_main) + result_money), 3)

    #                 if LongOrShort == 1:
    #                     total_procent = round(float(((OnlineCost - StartPlace)/StartPlace) * 100), 2)
    #                     LongOrShort = "Long"

    #                 else:
    #                     total_procent = round(float(((OnlineCost - StartPlace)/StartPlace) * 100), 2)
    #                     total_procent = total_procent * -1
    #                     LongOrShort = "Short"
                            

    #             last_list["TokenName"].append(TokenName)
    #             last_list["LongOrShort"].append(LongOrShort)
    #             last_list["Leverage"].append(Leverage)
    #             last_list["StartPlace"].append(StartPlace)
    #             last_list["MarkPrice"].append(OnlineCost)
    #             last_list["Procent"].append(total_procent)
    #             last_list["StopLoss"].append(StopLoss)
    #             last_list["TakeProfit"].append(TakeProfit)
    #             last_list["Fix_or_not"].append(None)


# def encrypt(num):
#     key = 7
#     encrypted_num = num * key
#     return encrypted_num

# def decrypt(encrypted_num):
#     key = 7
#     num = encrypted_num // key
#     return num

#     # Stop at no loss

# # Пример использования
# original_num = 324430515
# encrypted_num = encrypt(original_num)
# print(f"Зашифрованная цифра: {encrypted_num}")
# decrypted_num = decrypt(encrypted_num)
# print(f"Расшифрованная цифра: {decrypted_num}")
# if 1 != 1:
#     print(1)
# else:
#     print( 'Invalid request', 400)











# from flask import Flask, render_template, request, url_for, redirect, jsonify
# from flask_login import LoginManager, UserMixin, login_required ,logout_user ,login_user
# from flask_bootstrap import Bootstrap
# from MongoDB import Table
# from Data import *
# import requests
# import hashlib
# import hmac
# import json
# import urllib.parse


# db = Table(DataUrl)

# app = Flask(__name__)
# bootstrap = Bootstrap(app)



# app = Flask(__name__)

# def validate_telegram_request(data):
# 	query_id = data.get('query_id')
# 	user = data.get('user')
# 	auth_date = data.get('auth_date')
# 	hash_value = data.get('hash')

# 	if not query_id or not user or not auth_date or not hash_value:
# 		return False

#     # Декодирование строки используя URL-encoding
# 	decoded_user = urllib.parse.unquote(json.dumps(user))

#     # Формирование тела запроса
# 	body = f"auth_date={auth_date}\nquery_id={query_id}\nuser={decoded_user}"

#     # Получение хэша от токена вашего бота с помощью алгоритма HMAC-SHA256 с ключом WebAppData
# 	bot_token = TokenBot
# 	bot_token_hash = hmac.new(
#     	key=bytes("WebAppData", 'utf-8'),
#     	msg=bytes(bot_token, 'utf-8'),
#     	digestmod=hashlib.sha256
# 	).digest()

# 	# Получение хэша от тела запроса с использованием того же алгоритма и ключа
# 	body_hash = hmac.new(
#     	key=bot_token_hash,
#     	msg=bytes(body, 'utf-8'),
#     	digestmod=hashlib.sha256
# 	).hexdigest()

#     # Сравнение хэша с полученным значением хэша в запросе
# 	if body_hash == hash_value:
# 		print("True")
# 		return True
# 	else:
# 		print("False")
# 		print(body_hash, hash_value)
# 		return False

# def decrypt(encrypted_num):
# 	key = 45
# 	num = encrypted_num // key
# 	return num


# @app.route('/test/<int:encrypt_UserId>', methods=['POST', 'GET'])
# def test(encrypt_UserId):
# 	if request.method == "GET":
# 		show_input = True
# 		return render_template('test.html', show_input=show_input)

# 	if request.method == "POST":
# 		UserId = decrypt(encrypt_UserId)
# 		show_input = True
# 		WebName = request.form['ChannelName']

# 		if not db.CheckOnSame_WebName(WebName):
# 			db.Add_WebName(WebName = WebName, UserId = UserId)


# 			file_name = f"templates/user_{WebName}.html"

# 			with open(file_name, "w") as file:
# 				file.write(template_string)

# 			show_input=False
# 			return render_template('test.html', show_input=show_input)


# 		else:
# 			Same = "Такой канал уже есть"
# 			return render_template('test.html', show_input=show_input, Same = Same)

    

# @app.route('/OpenDeal/<string:WebName>', methods=['GET'])
# def user_site(WebName):
# 	print(111)
# 	data = request.args
# 	print(data)
# 	if validate_telegram_request(data):
# 		print(2)
# 		print(WebName)
# 		All_Positions = db.Get_Positions(WebName)
# 		print(All_Positions, "----------------------------------------------------")

# 		last_list = {"TokenName":[],
# 					"LongOrShort":[],
# 					"Leverage":[],
# 					"StartPlace":[],
# 					"MarkPrice":[],
# 					"Procent":[],
# 					"StopLoss":[],
# 					"TakeProfit":[],
# 					"Fix_or_not":[]
# 					}

# 		NonePos = 0
# 		for i in range(1, 4):
# 			num_for_value = i - 1
# 			Have_not = All_Positions[num_for_value][f'Position_{i}']['TokenName']
# 			if Have_not == None or Have_not == '':
# 				NonePos += 1
# 				if NonePos == 3:
# 					return render_template(f'user_{WebName}.html', NonePositions="Did not add positions", last_list = last_list)
# 			else:
# 				res = db.Check_Event_for_Positions(WebName=WebName, Num_position=i)

# 				num_i = All_Positions[num_for_value][f'Position_{i}']
# 				TokenName = num_i['TokenName']
# 				LongOrShort=num_i['LongOrShort']
# 				Leverage=num_i['Leverage']
# 				StartPlace=num_i['StartPlace']
# 				StopLoss=num_i['StopLoss']
# 				TakeProfit=num_i['TakeProfit']
# 				Money=num_i['Money']

# 				if res != None:
# 					last_list["TokenName"].append(TokenName)
# 					if LongOrShort == 1:
# 						LongOrShort = "Long"
# 					else:
# 						LongOrShort = "Short"
# 					last_list["LongOrShort"].append(LongOrShort)
# 					last_list["Leverage"].append(Leverage)
# 					last_list["StartPlace"].append(StartPlace)
# 					last_list["MarkPrice"].append(None)
# 					last_list["StopLoss"].append(StopLoss)
# 					last_list["TakeProfit"].append(TakeProfit)
# 					last_list["Fix_or_not"].append(res)

# 				else:

# 					url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={TokenName}&interval=1&limit=1"

# 					payload={}
# 					headers = {}

# 					response = requests.request("GET", url, headers=headers, data=payload)
# 					OnlineCost = f'{response.json().get("result").get("list")[0][2]}'
# 					OnlineCost = round(float(OnlineCost), 20)

#                   ###########################     FIXED     ############################


# 					if LongOrShort == 1:
# 						if TakeProfit != None:
# 							if OnlineCost >= float(TakeProfit):
# 								db.Event_for_Positions(WebName=WebName, TP_or_SL=1, Num_position=i)

# 					if LongOrShort == 1:
# 						if StopLoss != None:
# 							if OnlineCost <= float(StopLoss):
# 								db.Event_for_Positions(WebName=WebName, TP_or_SL=0, Num_position=i)

# 					if LongOrShort == 0:
# 						if TakeProfit != None:
# 							if OnlineCost <= float(TakeProfit):
# 								db.Event_for_Positions(WebName=WebName, TP_or_SL=1, Num_position=i)

# 					if LongOrShort == 0:
# 						if StopLoss != None:
# 							if OnlineCost >= float(StopLoss):
# 								db.Event_for_Positions(WebName=WebName, TP_or_SL=0, Num_position=i)

#                   ############################     END     #############################


# 					if Money != None:
# 						Money = int(Money)
# 						result_money = int(Money) * int(Leverage)
# 						procent_for_main = round(float((OnlineCost - StartPlace)/StartPlace), 4)
# 						# total_cost = round(float((result_money * procent_for_main) + result_money), 3)
# 						total_procent = round(float((((OnlineCost - StartPlace)/StartPlace) * 100) * Leverage), 2)
# 						main_profit = round(float(result_money * procent_for_main), 3)

# 						if LongOrShort == 1:
# 							LongOrShort = "Long"
# 							if total_procent >= 0:
# 								print(f"+{main_profit}(+{total_procent}%)")
# 							else:
# 								print(f"{main_profit}({total_procent}%)")

# 						else:
# 							total_procent = total_procent * - 1
# 							main_profit = main_profit * - 1
# 							LongOrShort = "Short"
# 							if total_procent >= 0:
# 								print(f"+{main_profit}(+{total_procent}%)")

# 							else:
# 								print(f"{main_profit}({total_procent}%)")


#               ###############################    Без MONEY Только Procent  #####################################

# 					else:
# 						procent_for_main = round(float((OnlineCost - StartPlace)/StartPlace), 4)
# 						# total_cost = round(float((result_money * procent_for_main) + result_money), 3)

# 						if LongOrShort == 1:
# 							total_procent = round(float(((OnlineCost - StartPlace)/StartPlace) * 100), 2)
# 							LongOrShort = "Long"

# 						else:
# 							total_procent = round(float(((OnlineCost - StartPlace)/StartPlace) * 100), 2)
# 							total_procent = total_procent * -1
# 							LongOrShort = "Short"


# 					last_list["TokenName"].append(TokenName)
# 					last_list["LongOrShort"].append(LongOrShort)
# 					last_list["Leverage"].append(Leverage)
# 					last_list["StartPlace"].append(StartPlace)
# 					last_list["MarkPrice"].append(OnlineCost)
# 					last_list["Procent"].append(total_procent)
# 					last_list["StopLoss"].append(StopLoss)
# 					last_list["TakeProfit"].append(TakeProfit)
# 					last_list["Fix_or_not"].append(None)


# 		return render_template(f'user_{WebName}.html', last_list=last_list)
# 	else:
# 		return 'Invalid request', 400
# 		# return app.send_static_file(file_name)



# @app.route('/AddPosition/<int:encrypt_UserId>', methods=['POST', 'GET']) #OpenDeal/ChannelBoss
# def AddPosition(encrypt_UserId):
# 	if request.method == "POST":
# 		# Logic that should only be executed once
#         print(1111)
# 		data = request.form
# 		print(data)
#       	# Далее обрабатываете данные из callback_data
# 		if validate_telegram_request(data):
# 			UserId = decrypt(encrypt_UserId)
# 			TokenName = str.upper(request.form['TokenName'])
# 			Leverage = int(request.form['Leverage'])
# 			try:
# 				StartPlace = float(request.form['StartPlace'])
# 			except ValueError:
# 				return render_template('AddPosition.html', error_StartPlace='Use only "." but not ","!')

# 			LongOrShort = int(request.form['radio'])

# 			if request.form['TakeProfit'] != "":
# 				TakeProfit = float(request.form['TakeProfit'])
# 			else:
# 				TakeProfit = None
# 			if request.form['StopLoss'] != "":
# 				StopLoss = float(request.form['StopLoss'])
# 			else:
# 				StopLoss = None
# 			if request.form['Money'] != "":
# 				Money = int(request.form['Money'])
# 			else:
# 				Money = None


#           #################      __errors__      #################

# 			if Leverage > 100:
# 				return render_template('AddPosition.html', error_TokenName="Leverage not be more 100x!")

# 			if TakeProfit != None and StopLoss != None:
# 				if LongOrShort == 1:
# 					if TakeProfit <= StopLoss: #long
# 						return render_template('AddPosition.html', error_TP_SL="Take Profit can't be more than StopLoss! (LONG)")

# 			if LongOrShort == 0:
# 				if TakeProfit >= StopLoss: #short
# 					return render_template('AddPosition.html', error_TP_SL="Take Profit can't be less than StopLoss! (SHORT)")

# 			url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={TokenName}&interval=1&limit=1"

# 			payload={}
# 			headers = {}

# 			response = requests.request("GET", url, headers=headers, data=payload)
# 			OnlineCost = f'{response.json().get("result")}'
# 			if OnlineCost != "{}":

# 				res = db.Add_Position(UserId = UserId, TokenName = TokenName, Money = Money, Leverage = Leverage, StartPlace = StartPlace,
# 									TakeProfit = TakeProfit, StopLoss = StopLoss, LongOrShort = LongOrShort)

# 			if res == True:
# 				return render_template('AddPosition.html', Success="Added position successfully")

# 			elif res == "All_Positions_full":
# 				return render_template('AddPosition.html', All_Positions_full="You have 3/3 positions! Please, delete someone")

# 			elif res == False:
# 				return render_template('AddPosition.html', Not_Found="You don't have a channel!")

# 			else:
# 				return render_template('AddPosition.html', error_TokenName="ByBit doesn't have that!")
              
# 		else:
# 			return 'Invalid request', 400

# 	return render_template('AddPosition.html')

















# if __name__ == "__main__":
# 	app.run(host='0.0.0.0', port=80)