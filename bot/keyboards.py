from aiogram import types


def kb():
    """Главный кнопки"""
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Продукция 📦"),
        types.KeyboardButton(text="Контакты 📩"),
        types.KeyboardButton(text="Новости 📝"),
        types.KeyboardButton(text="Наши сервисные центры ⚙"),
        types.KeyboardButton(text="Онлайн каталог 📓")
    )
    return keyboard


def pro():
    """кнопка для продукции"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='МОРОЗИЛКИ'),
        types.KeyboardButton(text='ВИТРИНЫ'),
        types.KeyboardButton(text='КОНДИЦИОНЕР'),
        types.KeyboardButton(text='ДОЗАТОРЫ ДЛЯ НАПИТКОВ'),
        types.KeyboardButton(text='ЛЕДЯНЫЕ МАШИНЫ'),
        types.KeyboardButton(text='КУЛЕР ДЛЯ ВОДЫ'),
        types.KeyboardButton(text='МИКРОВОЛНОВАЯ ПЕЧЬ'),
        types.KeyboardButton(text="Go Back")
    )
    return keyboard


def cabinets():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='ВИТРИНЫ МОРОЖЕНОГО'),
        types.KeyboardButton(text='КОНДИТЕРСКИЕ ВИТРИНЫ'),
        types.KeyboardButton(text="Go Back ->")
    )
    return keyboard


def kb1():
    """кнопки для МОРОЗИЛКИ"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="МОРОЗИЛНЫЕ КАМЕРЫ"),
        types.KeyboardButton(text="ОХЛАДИТЕЛИ ДЛЯ НАПИТОК"),
        types.KeyboardButton(text="ХОЛОДИЛЬНИКИ ДЛЯ БУТЫЛОК"),
        types.KeyboardButton(text="ПРЕМИУМ ОХЛАДИТЕЛИ"),
        types.KeyboardButton(text="ХОЛОДИЛЬНИКИ SUB-ZERO"),
        types.KeyboardButton(text="МОРОЗИЛКИ ДЛЯ СУПЕРМАРКЕТ"),
        types.KeyboardButton(text="Go Back ->")
    )
    return keyboard


def sm():
    """Кнопки для супермаркетной морозилки"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='Передние открытые'),
        types.KeyboardButton(text='Морозильные камеры.'),
        types.KeyboardButton(text='Холодильники'),
        types.KeyboardButton(text='ВИТРИНЫ ТИПА БАССЕЙНА'),
        types.KeyboardButton(text='Go Back->')
    )
    return keyboard


def counter_coolers():
    """ОХЛАДИТЕЛИ"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='Настолные охладители'),
        types.KeyboardButton(text='Охладители для напиток'),
        types.KeyboardButton(text='Охладители банок'),
        types.KeyboardButton(text='Go Back->')
    )
    return keyboard


def freezers():
    """кнопки для морозилки"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='Морозильные камеры'),
        types.KeyboardButton(text='Морозилник глухими кришки'),
        types.KeyboardButton(text='Энергоэффективный морозильники'),
        types.KeyboardButton(text='Вертикальный морозильники'),
        types.KeyboardButton(text='Go Back->')
    )
    return keyboard


