#!/usr/bin/env python
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio
import json
from aiogram.utils.chat_action import ChatActionSender




TOKEN="7614705035:AAFh5EPJtUwkh9gL4rwyUSQSX-IsNMhKNHM"
bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {}




@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif message.text == "📥 CV Yuklash" or message.text == '/cv':
        await cv_download_menu(message,bot)
    elif message.text == "📞 Bog'lanish" or message.text == '/contact':
        await contact(message)
    elif message.text == "🧑‍🏫 Ta'lim" or message.text == '/education':
        await education(message)
    elif message.text == "🧑‍💻 Tajriba" or message.text == '/experience':
        await tajriba(message)
    elif message.text == "⬅️ Orqaga":
        if user_data[user_id]["state"] in {"cv_download_menu", "contact", "education", "tajriba"}:
            await start(message)


@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🧑‍🏫 Ta'lim"), types.KeyboardButton(text="🧑‍💻 Tajriba"),],
         [types.KeyboardButton(text="📥 CV Yuklash"),types.KeyboardButton(text="📞 Bog'lanish")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"Assalomu Alaykum! Ushbu bot yordamida siz Rustamov Usmonning portfolio boti bilan tanishib chiqasiz.😊\n\n",reply_markup=keyboard)
    print(user_data)


@dp.message(Command(commands=["CV Yuklash 📥",'/cv']))
async def cv_download_menu(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "cv_download_menu"
    button = [
        [types.KeyboardButton(text=f"⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "data/Usmon_cv.pdf"
    file = FSInputFile(path=file_path)

    async with ChatActionSender.upload_document(bot=bot,chat_id=message.chat.id):
        await message.reply_document(document=file)
    await message.answer(f"Bu mening rezyumem. Yuklab oling! 😊", reply_markup=keyboard)
    print(user_data)


@dp.message(Command(commands=["📞 Bog'lanish",'/contact']))
async def contact(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "contact"
    button = [
        [types.KeyboardButton(text=f"⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"Men bilan bog'lanish uchun kontaktlar: \n\nhttps://t.me/@rustamov_0122 ✉️ \n\nTelefon raqam: +998-94-952-82-88 ☎️",reply_markup=keyboard)
    print(user_data)




@dp.message(Command(commands=["🧑‍🏫 Ta'lim",'/education']))
async def education(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "education"
    button = [
        [types.KeyboardButton(text=f"⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"Bu bo'limda siz mening qaysi ta'lim musassasida o'qiganim va qaysi kurslarni bitirganim haqida to'liq ma'lumot olasiz\n\n"
                         f"🇺🇸 Cambridge markazida ingliz tilining turli darajalari bo‘yicha chuqur bilimlarga ega bo‘ldim, jumladan Elementary, Pre-Intermediate,Intermediate va Upper Intermediate bosqichlarini muvaffaqiyatli tugatdim.Bundan tashqari IELTS kursni muvaffaqiyatli tugatganman.\n\n"
                         f"🧮 Qorakol ziyo matematika kursini muvaffaqiyatli tugatganman\n\n"
                         f"🏫 Bakalavr, Sun'iy Intellekt (AI)\n"
                         f"Amity University — Tashkent \nSentyabr 2023 — Hozirgi vaqtgacha\n"
                         f"2-kurs talabasiman.",reply_markup=keyboard)
    print(user_data)



@dp.message(Command("🧑‍💻 Tajriba"))
@dp.message(Command(commands=["🧑‍🏫 Ta'lim",'/experience']))
async def tajriba(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["state"] = "tajriba"
    button = [
        [types.KeyboardButton(text=f"⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f"🧑‍💻 Bu bo'limda siz mening tajribam haqida ma'lumot olasiz\n\n"
                         f"Euphoria kompaniyasida sotuv bo‘yicha menejer - 2024 yil \n\n"
                         f"Men Euphoria kompaniyasida sotuv menejeri sifatida faoliyat yuritganman. Ish faoliyatim davomida "
                         f"mijozlar bilan samarali aloqalar o‘rnatish, mahsulot va xizmatlarni targ‘ib qilish, sotuvlar "
                         f"hajmini oshirish bo‘yicha strategiyalar ishlab chiqish va joriy etish kabi vazifalarni "
                         f"muvaffaqiyatli bajarganman. Shuningdek, mijozlar ehtiyojlarini chuqur o‘rganib, ularga "
                         f"individual yondashuv asosida eng yaxshi yechimlarni taklif qilish orqali kompaniya daromadiga "
                         f"ijobiy hissa qo‘shganman.",reply_markup=keyboard)
    print(user_data)


async def main():
    print('The bot is running...')
    await dp.start_polling(bot)
asyncio.run(main())