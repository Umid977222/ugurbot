
def get_button(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Продукция 📦 ", request_contact=True),
        types.KeyboardButton(text="Контакты 📩 ", request_location=True),
        types.KeyboardButton(text="О нас 💬 ", request_location=True),
        types.KeyboardButton(text="Почему мы ⁉️", request_location=True),
        types.KeyboardButton(text="Наши магазины 🏪 ", request_location=True),
        types.KeyboardButton(text="Новости 📝 ", request_location=True),
        types.KeyboardButton(text="Наши сервисные центры ⚙️", request_location=True),
        types.KeyboardButton(text="Онлайн каталог 📓 ", request_location=True)
    )
