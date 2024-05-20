
from telebot import types
import config

# Reply_WebSetting = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
# Reply_WebSetting.add(types.KeyboardButton(text="My website"))
Inline_Only_My_Website = types.InlineKeyboardMarkup(row_width=1)
Inline_Only_My_Website.add(types.InlineKeyboardButton(text="My channel", callback_data="My_website"))


Inline_Main = types.InlineKeyboardMarkup(row_width=1)
Inline_Main.add(types.InlineKeyboardButton(text="INFO ❗️", callback_data="INFO"))
Inline_Main.add(types.InlineKeyboardButton(text='Example', web_app=types.WebAppInfo(url=f"{config.WEBHOOK_HOST}/OpenDeal/Example")))
Inline_Main.add(types.InlineKeyboardButton(text="My channel", callback_data="My_website"))

