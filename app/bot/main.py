import asyncio
import logging
import sys
import os 
import json
from datetime import date
from os.path import abspath


from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode, content_type
from aiogram.filters import CommandStart
from aiogram.types import ContentType, Message, update
from aiogram.filters.command import Command

load_dotenv()
TOKEN = os.getenv("TOKEN")

sys.path.append("../backend")
from priceChecker.priceCheck import price_check
from priceChecker.checkSocPrice import checkSocPrice



sys.path.append("../email")
#from email_sender import send

#print(TOKEN)
dp = Dispatcher()

async def update_json():
    global users_json
    with open("./db.json", "w") as file:
        json_object = json.dumps(users_json, indent=4)
        file.write(json_object)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("hello")


@dp.message(F.photo)
async def Photos(message: types.Message) -> None:
    global user_json
    

    if str(message.chat.id) not in users_json.keys():
        await message.answer("Сначала надо авторизоваться и ввсети свой номер телефона и почту")
        await message.answer("Введите номер телефона:")
    else:
        if message.caption is None:
            await message.answer("Пришлите фотографию с адресом магазина")
        else:
            await message.answer("фотогрфия сохранена")
            path = abspath(f"../backend/files/{message.caption}|{users_json[str(message.chat.id)][0]}|{users_json[str(message.chat.id)][1]}|{date.today()}.jpg")
            print(path)
            await message.bot.download(message.photo[-1].file_id, path)
            res = price_check(path, abspath("../backend/priceChecker/rostov_prices.json"))
            print(res)
            if res is None:
                return "Не удалось распознать ценник"
            if res[3] == 1:
                if int(checkSocPrice(res[1])[0]) < res[4]:
                    await message.answer("цена, как для социального ценника, завышена")
                    os.remove(path)
                await message.answer("цена, как для социального ценника, не завышена")
            else:
                os.remove(path)
                await message.answer("это не социальный ценник")

    """else:
        photo = message.photo[-1].file_id
        if not os.path.isdir(f"./photos/{date.today()}"):
            print("create dir")
            os.mkdir(f"./photos/{date.today()}")
        path_img = f"./photos/{date.today()}/{users_json[str(message.chat.id)][0]}.jpg"
        await message.bot.download(photo, destination=path_img)
        await send(path_img)
    """

@dp.message()
async def echo(message: Message):
    global users_json
    is_user = True
    for k, v in  users_json.items():
        print(message.chat.id, k)
        if message.chat.id == int(k):
            is_user = False
            print(v)
            if len(v) == 2:
                await message.answer("Вы уже ввели данные для аунтефикации")
            else:
                users_json[k].append(message.text)
                await update_json()
                await message.answer("Отлично теперь можете отправлять ценники и проверять их!")
    if is_user:
        users_json[message.chat.id] = [message.text]
        await update_json()

async def main() -> None:
    if TOKEN is not None:
        Token = str(TOKEN)
    else:
        print("TOKEN is not in .env file!")
        quit(1)
    bot = Bot(Token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    users_json = {}
    with open("./db.json", 'r') as file:
        users_json = json.load(file)
    print(users_json.items())
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
