from aiogram import types
from .control import dp
from .get_data import fetch
from .keyboards import kb, kb1, pro


@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    await message.answer(
        text=f"Hi bot {message.from_user.full_name}",
        reply_markup=kb()
    )


@dp.message_handler(text='Продукция 📦')
async def choice5(message: types.Message):
    await message.answer(
        text="Выбрайте", reply_markup=pro()
    )


@dp.message_handler(text='Контакты 📩')
async def choice5(message: types.Message):
    await message.answer(
        text=f'+998911655559'
             f'\n'
             f'\n+998971305559'
    )


@dp.message_handler(text='Новости 📝')
async def choice5(message: types.Message):
    await message.answer(
        text="Ожидайте скорых новостей"
    )


@dp.message_handler(text='Наши сервисные центры ⚙')
async def choice5(message: types.Message):
    await message.reply_location(
    )


@dp.message_handler(text='Go Back')
async def choice3(message: types.Message):
    await message.answer(
        text="->", reply_markup=kb()
    )


@dp.message_handler(text='Go Back ->')
async def choice(message: types.Message):
    await message.answer(
        text="->", reply_markup=pro()
    )


@dp.message_handler(text='Go Back->')
async def choice(message: types.Message):
    await message.answer(
        text="->", reply_markup=kb1()
    )


# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def lang(message: types.Message):
#     mes = message.text
#     res = await fetch()
#     for x in res:
#         name = x['product']
#         description = x['description']
#         if mes == x['product']:
#             await message.answer(f'{name}'
#                                  f'\n{description}'
#                                  )
#     if mes == 'Go Back.':
#         await message.answer(f'.', reply_markup=kb1())

