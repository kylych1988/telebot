
from aiogram import Bot, Dispatcher, executor, types

import config
import random

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','go'])
async def help(message: types.Message):
    await message.answer(f"Салам,{message.from_user.full_name} .Менин атым kylych.\nМен жөнүндө көбүрөөк билгиңиз келсе, басыңыз: /help ")
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Мен сага оюн сунуш кыла алам<< Randomer >>\nОюндун эрежелери:\n1) Менимче, 1ден 3кө чейинки сандарды сиз болжолдооңуз керек\n2) Сандарды гана жаз \n3) Эгер сиз санды тапсаңыз, 1 упай аласыз\n4) Текс жазбаныз  <<Кара>>\nМенин Коммандам:\n/start - Ботту иштетиңиз.\n/help - Жардам.\n/startgame - Оюнду баштаңыз")

@dp.message_handler(commands=['startgame'])
async def startgame(message: types.Message):
    await message.answer("Оюнга кош келиңиз. Мен 1ден 3кө чейинки санды табам, сиз таба аласызбы? :")

@dp.message_handler(text=["1","2","3",])
async def hello(message: types.Message):
    user = int(message.text)
    randomer = random.randint(1, 3)

    await message.answer(f"Сизге ийгилик{message.from_user.full_name} : ")

    print(user)
    if user == randomer:
        await message.reply(f"Сиз ойлодуңуз!!! Менин номерим: {randomer}")
        
    elif user != randomer:
        await message.reply(f"Сен ойлодунуз жоксуң!!! Менин номерим:{randomer} ")
        
        

executor.start_polling(dp)