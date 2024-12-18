from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Текст комманды /help
def help_command_handler(message):
    from bot import bot
    help_text = ( 
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом.\n"
        "/register - Зарегистрироваться в базе данных.\n"
        "/set_schedule_meeting - Запланировать встречу на определенное время.\n"
        "/set_free_meeting - Запланировать встречу на ближайшее свободное для всех участников время, учтем пожелания по самой ранней дате и времени.\n"
        "/view_meetings - Посмотреть все запланированные встречи на текущей неделе.\n"
        "/view_users- Посмотреть всех зарегистрированных пользователей.\n"
        "/delete_meeting - Удалить встречу по id.\n"
        "/stats - Показать статистику встреч и визуализацию загруженности.\n"
        "/cancel - Если посередине ввода данных внутри команды, вы передумали ей пользоваться и хотите выйти в меню команд\n"
    )
    bot.send_message(message.chat.id, help_text)

# Клавиатура со всеми командами
def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # Создаем клавиатуру
    button1 = KeyboardButton('/register')
    button2 = KeyboardButton('/help') 
    button3 = KeyboardButton('/set_schedule_meeting')
    button4 = KeyboardButton('/set_free_meeting') 
    button5 = KeyboardButton('/view_meetings') 
    button6 = KeyboardButton('/view_users') 
    button7 = KeyboardButton('/delete_meeting') 
    button8 = KeyboardButton('/stats')
    button9 = KeyboardButton('/cancel')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)  # Добавляем кнопки на клавиатуру
    return keyboard

# Клавиатура с командой /cancel
def create_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # Создаем клавиатуру
    button1 = KeyboardButton('/cancel')
    keyboard.add(button1)
    return keyboard

# Клавиатура с да/нет для команды /set_free_meeting, где мы подтверждаем (или не подтверждаем) сохранение встречи
def create_yes_no_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # Создаем клавиатуру
    button1 = KeyboardButton('да')
    button2 = KeyboardButton('нет')
    keyboard.add(button1, button2)
    return keyboard