from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from config import token
import logging
import asyncio

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["Uzb", "Rus"]
    keyboard.add(*buttons)
    await message.answer(
        text=f"Xush kelibsz {message.from_user.full_name}",
        reply_markup=keyboard
    ),
    await message.answer(
        text=f"Добро пожаловать {message.from_user.full_name}",
        reply_markup=keyboard
    )


@dp.message_handler(content_types=types.ContentType.TEXT)
async def choice_lang1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="ВСТРАИВАЕМАЯ ТЕХНИКА"),
        types.KeyboardButton(text="ВАРОЧНЫЙ ЦЕНТР"),
        types.KeyboardButton(text="КОНДИЦИОНЕРЫ"),
        types.KeyboardButton(text="ПОСУДОМОЕЧНЫЕ МАШИНЫ"),
        types.KeyboardButton(text="МИКРОВОЛНОВЫЕ ПЕЧИ"),
        types.KeyboardButton(text="ПЫЛЕСОС"),
        types.KeyboardButton(text="ХОЛОДИЛЬНИКИ"),
        types.KeyboardButton(text="Go Back")
    )
    language = message.text.title()
    if language == "Продукция 📦":
        msg = "Выберите категорию товаров:  ☑️",
        await message.answer(
            text="Выберите категорию товаров:  ☑️",
            reply_markup=keyboard
        )
    await message.answer(
        text=msg
    )


@dp.message_handler(content_types=types.ContentType.TEXT)
async def choice_lang(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Продукция 📦"),
        types.KeyboardButton(text="Контакты 📩"),
        types.KeyboardButton(text="О нас 💬"),
        types.KeyboardButton(text="Почему мы ⁉"),
        types.KeyboardButton(text="Наши магазины 🏪"),
        types.KeyboardButton(text="Новости 📝"),
        types.KeyboardButton(text="Наши сервисные центры ⚙"),
        types.KeyboardButton(text="Онлайн каталог 📓")
            )

    language = message.text.title()
    if language == "Uzb":
        msg = "Siz o'bek tilini tanladingiz"
    elif language == "Rus":
        msg = "Вы набрали руский язык"
        await message.answer(
            text="Выбрайте",
            reply_markup=keyboard
        )
    # await message.answer(
    #     text="tanlang",
    #     reply_markup=types.ReplyKeyboardRemove()
    # )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)