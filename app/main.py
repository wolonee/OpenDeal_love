from flask import Flask, render_template, request, url_for, redirect, jsonify, abort, send_file
#from flask_login import LoginManager, UserMixin, login_required ,logout_user ,login_user
from Buttons import *
from telebot import TeleBot, types
from datetime import datetime
# from pybit.unified_trading import HTTP
# from aiogram import Bot, Dispatcher, types
from MongoDB import Table
import time
import config
import requests
from utils import parse_init_data

Website_Event = None
Start_Event = None
db = Table(config.DataUrl)
list_for_BossChannel = []
IndexNextStep = 0
hideBoard = types.ReplyKeyboardRemove()

bot=TeleBot(config.BOT_TOKEN, parse_mode="HTML")
app = Flask(__name__)



def decrypt(encrypted_num):
    key = 45
    num = encrypted_num // key
    return num


def encrypt(num):
    key = 45
    encrypted_num = num * key
    return encrypted_num


@app.post(f"{config.WEBHOOK_PATH}")
def process_webhook_post():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


##############################       start        ################################# 


@bot.message_handler(commands=['start'])
def menu(message: types.Message):
    if message.chat.type == 'private':
        global Start_Event
        try:
            bot.delete_message(message.chat.id, Start_Event.message_id)
        except:
            pass
        if not db.CheckRegistr(message.from_user.id): # message.from_user.id - id человека который общается с ботом                                       # В этой строке моя функция принимает ^^^^^^ и проверяет есть ли этот id в БД
            start_command = message.text
            referal_id = str(start_command[7:])

            if str(referal_id) != "":
                if str(referal_id) != str(message.from_user.id):
                    db.AddUser(message.from_user.id, referal_id)
                    WebName_ref = db.Check_WebName(referal_id)
                    if WebName_ref != False:
                        Inline_Referal_WebApp = types.InlineKeyboardMarkup(row_width=1)
                        Inline_Referal_WebApp.add(types.InlineKeyboardButton(text=WebName_ref, web_app=types.WebAppInfo(url=f"{config.WEBHOOK_HOST}/OpenDeal/{WebName_ref}")))
                        bot.send_message(message.chat.id, f'Нажмите на кнопу чтобы посмотреть позиции\n\n<tg-spoiler><i>Нажмите /start чтобы перейти в главное меню</i></tg-spoiler>', reply_markup=Inline_Referal_WebApp, parse_mode='HTML')
                    else:
                        bot.send_message(message.chat.id, 'У владельца канала нет сайта для просмотра позиций, если есть возможность предупредите его об этом')

                else:
                    Start_Event = bot.send_message(message.chat.id, f"Приветствуем вас в <b>OpenDeal</b>\n\nВнизу вы можете найти всё, для навигации:", reply_markup=Inline_Main ,parse_mode='HTML')
            else:
                db.AddUser(message.from_user.id) 
                Start_Event = bot.send_message(message.chat.id, f"Приветствуем вас в <b>OpenDeal</b>\n\nВнизу вы можете найти всё, для навигации:", reply_markup=Inline_Main ,parse_mode='HTML')        
        else:
            start_command = message.text
            referal_id = str(start_command[7:])
            print(referal_id)

            if str(referal_id) != "":
                if str(referal_id) != str(message.from_user.id):
                    WebName_ref = db.Check_WebName(int(referal_id))
                    if WebName_ref != False:
                        Inline_Referal_WebApp = types.InlineKeyboardMarkup(row_width=1)
                        Inline_Referal_WebApp.add(types.InlineKeyboardButton(text=WebName_ref, web_app=types.WebAppInfo(url=f"{config.WEBHOOK_HOST}/OpenDeal/{WebName_ref}")))
                        bot.send_message(message.chat.id, f'Нажмите на кнопу чтобы посмотреть позиции\n\n<tg-spoiler><i>Нажмите /start чтобы перейти в главное меню</i></tg-spoiler>', reply_markup=Inline_Referal_WebApp, parse_mode='HTML')
                    else:
                        bot.send_message(message.chat.id, 'У владельца канала нет сайта для просмотра позиций, если есть возможность предупредите его об этом')
                else:
                    Start_Event = bot.send_message(message.chat.id, f"Приветствуем вас в <b>OpenDeal</b>\n\nВнизу вы можете найти всё, для навигации:", reply_markup=Inline_Main ,parse_mode='HTML')
            else:
                Start_Event = bot.send_message(message.chat.id, f"Приветствуем вас в <b>OpenDeal</b>\n\nВнизу вы можете найти всё, для навигации:", reply_markup=Inline_Main ,parse_mode='HTML')
      

###################################          channel_boss         ######################################

@bot.message_handler(commands=["channel_boss"])
def channel(message: types.Message):

    if message.chat.type == 'private':
        bot.delete_message(message.chat.id, message.message_id - 1)
        result = db.CheckRegistr(message.from_user.id)
        if result:
            user = db.Check_WebName(message.from_user.id)
                
            if user == False:
                Inline_Confirmation = types.InlineKeyboardMarkup(row_width=1)
                Inline_Confirmation.add(types.InlineKeyboardButton(text=f'Да, я подтверждаю', callback_data="Confirmation_True"))
                Inline_Confirmation.add(types.InlineKeyboardButton(text=f'Нет, я просто хотел посмотреть', callback_data="Confirmation_False"))

                bot.send_message(message.chat.id, '<b>Подтвердите, что в вашем канале есть более 100 АКТИВНЫХ подписчиков</b>\n\n<i>Иначе TakeProfit и StopLoss могут работать не корректно, из-за частого отсутствия обновления страницы со сделками</i>', reply_markup=Inline_Confirmation, parse_mode='HTML')

            else:
                bot.send_message(message.chat.id, 'У вас уже есть сайт', reply_markup=Inline_Only_My_Website)
        else:
            bot.send_message(message.chat.id, "Нет такого юзера, нажмите /start")

 
#######################         ОТВЕТ СЕРВЕРА         ###############################

@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):   
    WebName = webAppMes.web_app_data.data
    UserId = webAppMes.from_user.id
    print(WebName, UserId)

    file_name = f"templates/user_{WebName}.html"

    with open(file_name, "w") as file:
        file.write(config.template_string)

    db.Add_WebName(WebName = WebName, UserId = UserId)
    bot.send_message(webAppMes.chat.id, f"<b>Сайт успешно добавлен!</b>", reply_markup=hideBoard, parse_mode='HTML')
    time.sleep(1)
    bot.send_message(webAppMes.chat.id, f"Нажмите чтобы перейти в меню", parse_mode='HTML', reply_markup=Inline_Only_My_Website)


###################################         Мой сайт       ###############################################


@bot.message_handler(content_types=["text"])
def Reply_buttons(message: types.Message):
    
    if message.text == 'DFU':
        dt = db.Count_Data()
        bot.send_message(message.chat.id, f'All Users We have: <b>{dt[0]}</b>\n\nWhich of them has a website: <b>{dt[1]}</b>', reply_markup=None, parse_mode='HTML')
    
    if message.text == 'DeleteChannel12267':
        a = db.Delete_Channel(message.from_user.id)
        if a == True:
            bot.send_message(message.chat.id, f'<b>Удалён</b>', reply_markup=None, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, f'<b>Ошибка</b>', reply_markup=None, parse_mode='HTML')

#####################################     callback_query_handler     ################################################


@bot.callback_query_handler(lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'OPEN_USER_SITE':
                WebName = db.Check_WebName(call.from_user.id)
                if WebName == False:
                    bot.send_message(call.message.chat.id, f'У вас еще нет своего сайта\n\nЕсли вы являетесь <b>владельцем</b> канала, нажмите на <b>/channel_boss</b>', reply_markup=None, parse_mode='HTML')
                else:
                    pass

            elif call.data == 'INFO':
                Inline_Info_Back = types.InlineKeyboardMarkup(row_width=1)
                Inline_Info_Back.add(types.InlineKeyboardButton(text="<< Back", callback_data='Back_in_delete'))

                bot.send_message(call.message.chat.id, f'<b>Админ канала <u>сам</u> выставляет все данные об позиции:</b>\n\nOpenDeal никаким образом не причастен к его бирже.\n'
                'Поэтому всегда проверяйте данные по сделке, чтобы не стать жертвой "Фомо"\n\n— <tg-spoiler>Ты должен понимать, что этот проект неинтересен скамеру. '
                'Ведь зачем тогда ему показывать свои позиции онлайн? Ему не выгодно чтобы вы видели его убытки.\n\n'
                'Для профессионала ошибки это\nлишь часть пути.\nИ показывая их абсолютно всем, согласитесь он заслуживает доверие.</tg-spoiler>\n\n'
                '-----------------------------------------------\n'
                '\n<b>Добавление позиций:</b>\n\nДоступны только фьючерсы.\nДля спотовой торговли можно взять 1x плечо, '
                'но убедитесь, что этот койн существует на Bybit в виде фьючерсного контракта'
                '\n\nПри добавлении позиций вводите данные точно как в Bybit\n'
                '<tg-spoiler>(Некоторые койны сокращены на пару нулей для простоты восприятия)</tg-spoiler>', reply_markup=Inline_Info_Back, parse_mode='HTML')

            elif call.data == 'My_website':

                # bot.delete_message(call.message.chat.id, call.message.message_id)
                result = db.CheckRegistr(call.from_user.id)
                if result:
                    WebName = db.Check_WebName(call.from_user.id)


                    if WebName == False:
                        bot.send_message(call.message.chat.id, f'У вас еще нет своего сайта\n\nЕсли вы являетесь <b>владельцем</b> канала, нажмите на <b>/channel_boss</b>', reply_markup=None, parse_mode='HTML')
                            
                    else:
                        global Website_Event
                        try:
                            bot.delete_message(call.message.chat.id, Website_Event.message_id)
                        except:
                            pass
                        encrypt_UserId = encrypt(call.from_user.id)
                        Inline_MyWebApp = types.InlineKeyboardMarkup(row_width=1)
                        Inline_MyWebApp.add(types.InlineKeyboardButton(text=f'{WebName}', web_app=types.WebAppInfo(url=f"{config.WEBHOOK_HOST}/OpenDeal/{WebName}")))
                        Inline_MyWebApp.add(types.InlineKeyboardButton(text="Add Position", web_app=types.WebAppInfo(url=f"{config.WEBHOOK_HOST}/AddPosition")))
                        Inline_MyWebApp.add(types.InlineKeyboardButton(text="Delete Position", callback_data='Delete_Position'))
                        #bot.send_message(call.message.chat.id, 'Прогружаем сайт...', reply_markup=[None])
                        Website_Event = bot.send_message(call.message.chat.id, f"Ваша ссылка для просмотра вашими подписчиками:\n\n<tg-spoiler><code>t.me/OpenDealBot?start={call.from_user.id}</code></tg-spoiler>", reply_markup=Inline_MyWebApp, parse_mode='HTML')
                        
                else:
                    bot.send_message(call.message.chat.id, "<b>Нет такого юзера, нажмите /start</b>", parse_mode='HTML')

            elif call.data == 'Confirmation_True':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                Reply_WebName = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                Reply_WebName.add(types.KeyboardButton(text="Add Channel", web_app=types.WebAppInfo(url=f"{config.WEBHOOK_HOST}/AddChannel")))          
                bot.send_message(call.message.chat.id, 'Registration', reply_markup=Reply_WebName)
            elif call.data == 'Confirmation_False':
                bot.send_message(call.message.chat.id, f"Спасибо, продолжайте следить за сделками других каналов", reply_markup=hideBoard, parse_mode='HTML')

            elif call.data == "Delete_Position":
                WebName = db.Check_WebName(call.from_user.id)
                All_Positions = db.Get_Positions(WebName)
                Inline_Del_Pos = types.InlineKeyboardMarkup(row_width=1)
                NonePos = 0
                for i in range(1, 4):
                    num_for_value = i - 1
                    TokenName_n = All_Positions[num_for_value][f'Position_{i}']['TokenName']
                    if TokenName_n == '':
                        NonePos += 1
                        if NonePos == 3:
                            bot.send_message(call.message.chat.id, 'У вас нет открытых позиций')

                    else:
                        Inline_Del_Pos.add(types.InlineKeyboardButton(text=TokenName_n, callback_data=f'Del_Position_{i}'))
                
                Inline_Del_Pos.add(types.InlineKeyboardButton(text="<< Back", callback_data='Back_in_delete'))
                bot.send_message(call.message.chat.id, 'Нажмите на позицию чтобы удалить:', reply_markup=Inline_Del_Pos)

            elif call.data == "Del_Position_1":
                del_pos = db.Delete_Positions(UserId=call.from_user.id, Position_num=1)
                if del_pos == True:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.answer_callback_query(call.id, text='Позиция успешно удалена')
                else:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.send_message(call.message.chat.id, 'Ошибка, нажмите /start или напишите в поддержку')

            elif call.data == "Del_Position_2":
                del_pos = db.Delete_Positions(UserId=call.from_user.id, Position_num=2)
                if del_pos == True:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.answer_callback_query(call.id, text='Позиция успешно удалена')
                else:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.send_message(call.message.chat.id, 'Ошибка, нажмите /start или напишите в поддержку')


            elif call.data == "Del_Position_3":
                del_pos = db.Delete_Positions(UserId=call.from_user.id, Position_num=3)
                if del_pos == True:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.answer_callback_query(call.id, text='Позиция успешно удалена')
                else:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.send_message(call.message.chat.id, 'Ошибка, нажмите /start или напишите в поддержку')


            elif call.data == "Back_in_delete":
                bot.delete_message(call.message.chat.id, call.message.message_id)

    except Exception as Exc:
        print("Except :", Exc)



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$           FLASK           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

@app.route('/AddChannel', methods=['POST', 'GET'])
def test():

    if request.method == "GET":
        show_input = True
        return render_template('test.html', show_input=show_input)

    if request.method == "POST":

        show_input = True
        WebName = request.form['ChannelName']

        if not db.CheckOnSame_WebName(WebName):

            show_input=False
            return render_template('test.html', show_input=show_input)


        else:
            Same = "There is already one, pls take another"
            return render_template('test.html', show_input=show_input, Same = Same)


@app.route('/OpenDeal/<string:WebName>', methods=['GET'])
def user_site(WebName):

    All_Positions = db.Get_Positions(WebName)
    print(All_Positions, "----------------------------------------------------")

    last_list = {"TokenName":[],
                "LongOrShort":[],
                "Leverage":[],
                "StartPlace":[],
                "MarkPrice":[],
                "Procent":[],
                "StopLoss":[],
                "TakeProfit":[],
                "Link_with_post":[],
                "Fix_or_not":[]
                }

    NonePos = 0
    for i in range(1, 4):
        num_for_value = i - 1
        Have_not = All_Positions[num_for_value][f'Position_{i}']['TokenName']
        if Have_not == None or Have_not == '':
            NonePos += 1
            if NonePos == 3:
                return render_template(f'user_{WebName}.html', NonePositions="Did not add positions", last_list = last_list)
        else:
            res = db.Check_Event_for_Positions(WebName=WebName, Num_position=i)

            num_i = All_Positions[num_for_value][f'Position_{i}']
            TokenName = num_i['TokenName']
            LongOrShort=num_i['LongOrShort']
            Leverage=num_i['Leverage']
            StartPlace=num_i['StartPlace']
            Link_with_post=num_i['Link_with_post']
            StopLoss=num_i['StopLoss']
            TakeProfit=num_i['TakeProfit']
            Money=num_i['Money']

            if res != None:
                last_list["TokenName"].append(TokenName)
                if LongOrShort == 1:
                    LongOrShort = "Long"
                else:
                    LongOrShort = "Short"
                last_list["LongOrShort"].append(LongOrShort)
                last_list["Leverage"].append(Leverage)
                last_list["StartPlace"].append(StartPlace)
                last_list["MarkPrice"].append(None)
                last_list["Link_with_post"].append(Link_with_post)
                last_list["StopLoss"].append(StopLoss)
                last_list["TakeProfit"].append(TakeProfit)
                last_list["Fix_or_not"].append(res)
                last_list["Procent"].append(None)

            else:

                url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={TokenName}&interval=1&limit=1"

                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)
                OnlineCost = f'{response.json().get("result").get("list")[0][2]}'
                OnlineCost = round(float(OnlineCost), 20)
                print(OnlineCost)

                ###########################     FIXED     ############################


                if LongOrShort == 1:
                    if TakeProfit != None:
                        if OnlineCost >= float(TakeProfit):
                            db.Event_for_Positions(WebName=WebName, TP_or_SL=1, Num_position=i)

                if LongOrShort == 1:
                    if StopLoss != None:
                        if OnlineCost <= float(StopLoss):
                            db.Event_for_Positions(WebName=WebName, TP_or_SL=0, Num_position=i)

                if LongOrShort == 0:
                    if TakeProfit != None:
                        if OnlineCost <= float(TakeProfit):
                            db.Event_for_Positions(WebName=WebName, TP_or_SL=1, Num_position=i)
                
                if LongOrShort == 0:
                    if StopLoss != None:
                        if OnlineCost >= float(StopLoss):
                            db.Event_for_Positions(WebName=WebName, TP_or_SL=0, Num_position=i)

                ############################     END     #############################


                if Money != None:
                    Money = int(Money)
                    result_money = int(Money) * int(Leverage)
                    procent_for_main = round(float((OnlineCost - StartPlace)/StartPlace), 4)
                    # total_cost = round(float((result_money * procent_for_main) + result_money), 3)
                    total_procent = round(float((((OnlineCost - StartPlace)/StartPlace) * 100) * Leverage), 2)
                    main_profit = round(float(result_money * procent_for_main), 3)

                    if LongOrShort == 1:
                        LongOrShort = "Long"
                        if total_procent >= 0:
                            print(f"+{main_profit}(+{total_procent}%)")
                        else:
                            print(f"{main_profit}({total_procent}%)")

                    else:
                        total_procent = total_procent * - 1
                        main_profit = main_profit * - 1
                        LongOrShort = "Short"
                        if total_procent >= 0:
                            print(f"+{main_profit}(+{total_procent}%)")

                        else:
                            print(f"{main_profit}({total_procent}%)")


            ###############################    Без MONEY Только Procent  #####################################

                else:
                    procent_for_main = round(float((OnlineCost - StartPlace)/StartPlace), 4)
                    # total_cost = round(float((result_money * procent_for_main) + result_money), 3)

                    if LongOrShort == 1:
                        total_procent = round(float((((OnlineCost - StartPlace)/StartPlace) * 100) * Leverage), 2)
                        LongOrShort = "Long"

                    else:
                        total_procent = round(float((((OnlineCost - StartPlace)/StartPlace) * 100) * Leverage), 2)
                        total_procent = total_procent * -1
                        LongOrShort = "Short"


                last_list["TokenName"].append(TokenName)
                last_list["LongOrShort"].append(LongOrShort)
                last_list["Leverage"].append(Leverage)
                last_list["StartPlace"].append(StartPlace)
                last_list["MarkPrice"].append(OnlineCost)
                last_list["Procent"].append(total_procent)
                last_list["Link_with_post"].append(Link_with_post)
                last_list["StopLoss"].append(StopLoss)
                last_list["TakeProfit"].append(TakeProfit)
                last_list["Fix_or_not"].append(None)

    print(last_list)
    return render_template(f'user_{WebName}.html', last_list=last_list)



@app.route('/AddPosition', methods=['POST', 'GET'])
def AddPosition():
    if request.method == "GET":
        return render_template('AddPosition.html')
        
    if request.method == "POST":
        if request.headers.get('Content-Type') == 'application/json':
            data = request.json         
            print(data)
            init_data = parse_init_data(token=config.BOT_TOKEN, raw_init_data=data['initData'])
            if init_data is False:
                return jsonify({'UserInitData': f'Не удалось вас проверить на подлинность,\nнапишите в поддержку'})
            Money = None
            UserId = int(data.get('UserId'))
            TokenName = str.upper(data.get('TokenName'))
            Leverage = int(data.get('Leverage'))
            LongOrShort = int(data.get('LongOrShort'))
            Link_with_post = str(data.get('Link_with_post'))

            if "https://t.me/" in Link_with_post:
                pass
            else:
                return jsonify({'error_Link': "It's not telegram link"})

            try:
                StartPlace = float(data.get('StartPlace'))
            except ValueError:
                return jsonify({'error': 'Use only "." but not ","!'})
              
            if data.get('TakeProfit') != '':
                try:
                    TakeProfit = float(data.get('TakeProfit'))
                except ValueError:
                    return jsonify({'error': 'Use only "." but not ","!'})
            else:
                TakeProfit = None
                
            if data.get('StopLoss') != '':
                try:
                    StopLoss = float(data.get('StopLoss'))
                except ValueError:
                    return jsonify({'error': 'Use only "." but not ","!'})
            else:
                StopLoss = None
                
                
#            if data.get('Money') != '':
#                Money = int(request.form['Money'])
#            else:
#                Money = None


            #################      __errors__      #################

            if Leverage > 100:
                return jsonify({'error_Leverage': 'Leverage not be more 100x!'})

            if TakeProfit != None and StopLoss != None:
                if LongOrShort == 1:
                    if TakeProfit <= StopLoss: #long
                        return jsonify({"error_TP_SL": "Take Profit can't be more than StopLoss! (LONG)"})

                elif LongOrShort == 0:
                    if TakeProfit >= StopLoss: #short
                        return jsonify({"error_TP_SL": "Take Profit can't be less than StopLoss! (SHORT)"})
                  
            ################## ____________________ #################
            url = f"https://api.bybit.com/v5/market/mark-price-kline?category=linear&symbol={TokenName}&interval=1&limit=1"
            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            OnlineCost = f'{response.json().get("result")}'
            if OnlineCost != "{}":
                res = db.Add_Position(UserId = UserId, TokenName = TokenName, Money = Money, Leverage = Leverage, StartPlace = StartPlace,
                                    Link_with_post = Link_with_post, TakeProfit = TakeProfit, StopLoss = StopLoss, LongOrShort = LongOrShort)

                if res == True:
                    return jsonify({"Success": "Added position successfully"})

                elif res == "All_Positions_full":
                    return jsonify({"All_Positions_full": "You have 3/3 positions! Please,\ndelete someone"})

                elif res == False:
                    return jsonify({"Not_Found": "You don't have a channel!"})

            else:
                return jsonify({"error_TokenName": "ByBit doesn't have that!"})
        else:
            print("Server_Mistake: Content-type")
            return jsonify({"Server_Mistake": "Content-type, напишите в поддержку"})



def main():
    bot.delete_webhook()
    bot.set_webhook(config.WEBHOOK_URL)

    app.run(host=config.WEBAPP_HOST, port=config.WEBAPP_PORT)

if __name__ == '__main__':
    main()
    #telegram_bot(token)


# Админам:

# Вам ничего не нужно делать. Вы просто добавляете позицию и до тейка/стоп-лосса она будет всегда активна.
# Даже когда позиция дойдет до отметки, она просто зафиксируется в положении тейка/стоп-лосса, пока вы не добавите новую позицию,
# которая самостоятельно замениться на фиксированную.

# Доверие. На него уходят годы. Но наблюдая за сделками онлайн. Человек сразу
# Доверие. На него уходят годы. Но наблюдая за сделками в реальном времени, админ канал демонстрирует свою честность и надежность.

# Ты должен понимать, что этот проект неинтересен || скамеру. ||
# Ведь зачем тогда ему показывать свои позиции онлайн? Ему не выгодно чтобы вы видели его убытки.
# Для профессионала ошибки лишь часть пути. И показывая их абсолютно всем, согласитесь он правда заслуживает доверие.

    #schedule.every().day.at("21:28").do(function_to_run)
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    #Thread(target=schedule_checker).start()
    #bot.infinity_polling()

# git add --all

# git commit -m "Initial commit"

# git push -u origin main