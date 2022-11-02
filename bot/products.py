from aiogram import types
from .control import dp
from .get_data import fetch

"""
    ВИТРИНЫ
"""


@dp.message_handler(text='ВИТРИНЫ МОРОЖЕНОГО')
async def prod(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'ICE SHOW':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='КОНДИТЕРСКИЕ ВИТРИНЫ')
async def prod(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'CABINETS':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    КОНДИЦИОНЕР
"""


@dp.message_handler(text='КОНДИЦИОНЕР')
async def prod1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'CONDITIONERS':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    ДОЗАТОРЫ
"""


@dp.message_handler(text='ДОЗАТОРЫ ДЛЯ НАПИТКОВ')
async def prod2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'DISPENSERS':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    ЛЕДЯНЫЕ
"""


@dp.message_handler(text='ЛЕДЯНЫЕ МАШИНЫ')
async def prod3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'ICE MACHINES':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    КУЛЕР ДЛЯ ВОДЫ
"""


@dp.message_handler(text='КУЛЕР ДЛЯ ВОДЫ')
async def prod4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'WATER':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )

"""
    МИКРОВОЛНОВАЯ ПЕЧЬ
"""


@dp.message_handler(text='МИКРОВОЛНОВАЯ ПЕЧЬ')
async def prod5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == 'MICRO':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )

