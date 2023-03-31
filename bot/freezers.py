from aiogram import types
from .control import dp
from .get_data import fetch
from .keyboards import kb1, counter_coolers, sm, freezers, cabinets

"""
    ВИТРИНЫ
"""


@dp.message_handler(text='ВИТРИНЫ')
async def products(message: types.Message):
    await message.answer(text='ВИТРИНЫ', reply_markup=cabinets())


"""
    МОРОЗИЛКИ
"""


@dp.message_handler(text='МОРОЗИЛКИ')
async def choice_lang2(message: types.Message):
    await message.answer(text='.', reply_markup=kb1())


@dp.message_handler(text='МОРОЗИЛНЫЕ КАМЕРЫ')
async def choice_lang1(message: types.Message):
    await message.answer(f'..', reply_markup=freezers())


@dp.message_handler(text='Морозильные камеры')
async def choice_lan(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '6':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Морозилник глухими кришки')
async def choice_lan1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '3':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Энергоэффективный морозильники')
async def choice_lan2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '10':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Вертикальный морозильники')
async def choice_lan3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '16':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    ОХЛАДИТЕЛИ
"""


@dp.message_handler(text='ОХЛАДИТЕЛИ ДЛЯ НАПИТОК')
async def choice_lang3(message: types.Message):
    await message.answer(f'Охладители...', reply_markup=counter_coolers())


@dp.message_handler(text='Настолные охладители')
async def choice_las(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '7':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go_Back."))
    await message.answer(
     text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Охладители для напиток')
async def choice_las1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '4':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go_Back."))
    await message.answer(
     text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Охладители банок')
async def choice_las2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '1':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go_Back."))
    await message.answer(
     text="Выбрайте", reply_markup=keyboard
    )


"""
    ХОЛОДИЛЬНИКИ ДЛЯ БУТЫЛОК
"""


@dp.message_handler(text='ХОЛОДИЛЬНИКИ ДЛЯ БУТЫЛОК')
async def choice_lang4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '8':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back->"))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    ПРЕМИУМ ОХЛАДИТЕЛИ
"""


@dp.message_handler(text='ПРЕМИУМ ОХЛАДИТЕЛИ')
async def choice_lang5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '15':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back->"))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    ХОЛОДИЛЬНИКИ SUB-ZERO
"""


@dp.message_handler(text='ХОЛОДИЛЬНИКИ SUB-ZERO')
async def choice_lang6(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '17':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="Go Back->"))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


"""
    МОРОЗИЛКИ ДЛЯ СУПЕРМАРКЕТ
"""


@dp.message_handler(text='МОРОЗИЛКИ ДЛЯ СУПЕРМАРКЕТ')
async def choice_lang7(message: types.Message):
    await message.answer(f'ДЛЯ СУПЕРМАРКЕТ', reply_markup=sm())


@dp.message_handler(text='Передние открытые')
async def choice_lad(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '11':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="GoBack."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Морозильные камеры.')
async def choice_lad1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '18':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="GoBack."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='Холодильники')
async def choice_lad2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '19':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="GoBack."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(text='ВИТРИНЫ ТИПА БАССЕЙНА')
async def choice_lad2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    res = await fetch()
    for x in res:
        name = x['product']
        if x['category'] == '20':
            keyboard.add(types.KeyboardButton(text=name))
    keyboard.add(types.KeyboardButton(text="GoBack."))
    await message.answer(
        text="Выбрайте", reply_markup=keyboard
    )


@dp.message_handler(content_types=types.ContentType.TEXT)
async def lang(message: types.Message):
    mes = message.text
    res = await fetch()
    for x in res:
        name = x['product']
        description = x['description']
        if mes == x['product']:
            await message.answer_photo(x['img'])
            await message.answer(f'{name}'
                                 f'\n{description}'
                                 )
    if mes == 'Go Back.':
        await message.answer(f'.', reply_markup=freezers())
    elif mes == 'Goback.':
        await message.answer(f'.', reply_markup=sm())
    elif mes == 'Go_Back.':
        await message.answer(f'.', reply_markup=counter_coolers())
