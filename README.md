# Telegram Bot for Meeting Management via Google Calendar

Этот проект представляет собой Telegram-бота, который позволяет управлять встречами для двух или трех участников. Бот предоставляет интерфейс для планирования встреч, работы с пользователями, сбора статистики и отправки уведомлений. В данном документе описаны основные функции бота, его установка и использование.

## Содержание

1. [Требования](#требования)
2. [Установка](#установка)
3. [Использование](#использование)
4. [Команды](#команды)
5. [Структура кода](#структура-кода)


## Требования

Для работы бота необходимо следующее:
- Python 3.6 или выше
- Установленные библиотеки:
  - `telebot` для работы с Telegram API
  - `python-dotenv` для работы с переменными окружения
  - Другие библиотеки, необходимые для работы с Google API

## Установка

### 1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourbotrepository.git
   cd yourbotrepository
   ```

### 2. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Создайте файл `.env` в корневой директории проекта и добавьте свой Telegram токен, который вы получили от BotFather:
   ```
   TOKEN=ваш_токен
   ```

### 4. Настройка Базы данных

В проекте мы используме базу данных bot_database.db

Создайте нужные таблицы с помощью этих sql кодов:
```
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    user_id INTEGER NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```
CREATE TABLE IF NOT EXISTS meetings (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY,
    meeting_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    status TEXT DEFAULT 'pending',
    FOREIGN KEY (meeting_id) REFERENCES meetings (id) ON DELETE CASCADE
);
```
Запустите коды в DB Browser для SQLite


### 5. Google API: 
Получите файл credentials.json для доступа к Google API и поместите его в корневую папку проекта.

сейчас пойдет мясо

#### Шаг 1: Создание проекта в Google Cloud Console
Перейдите на Google Cloud Console:

Откройте Google Cloud Console. Войдите в свой Google аккаунт

Создайте новый проект:

Нажмите на выпадающее меню в верхней части страницы (где написано "Select a project") и выберите "New Project".

Задайте имя проекту, нажмите "Create".

#### Шаг 2: Включение необходимых API

Включите API:
В меню слева выберите "APIs & Services" → "Library".
Найдите и выберите API "Google Calendar API".

Нажмите кнопку "Enable", чтобы включить API для вашего проекта.

#### Шаг 3: Создание учетных данных

Создайте учетные данные:

В меню слева выберите "APIs & Services" → "Credentials" → "Create Credentials" → "OAuth client ID".

Настройка OAuth Consent Screen:

Перед созданием учетных данных вам может быть предложено настроить экран согласия OAuth.

Выберите "External", укажите необходимые данные (название приложения, адрес электронной почты поддержки и т.д.).

Добавьте свою почту в test_users

Выберите тип приложения:

Для настольного приложения выберите "Desktop app".

Укажите название клиента ("My Desktop Client" по дефолту) и нажмите "Create".

Сохраните файл credentials.json в корневом каталоге вашего проекта.


## Использование

Запустите бота, выполнив следующую команду:

```bash
python bot.py
```

После запуска бот будет готов к приему команд от пользователей в Telegram.

## Команды

Бот поддерживает следующие команды:

- `/start` - Запускает бота и предоставляет пользователю информацию о доступных командах.
- `/register` - Регистрирует пользователя и добавляет его в базу данных.
- `/help` - Выводит список доступных команд.
- `/set_schedule_meeting` - Позволяет установить встречу на определенное время для участников.
- `/set_free_meeting` - Устанавливает встречи на свободное время между участниками.
- `/delete_meeting` - Удаляет встречу из расписания.
- `/view_meetings` - Позволяет просмотреть все запланированные встречи.
- `/view_users` - Просматривает всех зарегистрированных пользователей.
- `/stats` - Генерирует и отображает статистику встреч за неделю.
- `/google_authentication` - Процесс аутентификации пользователя через Google.
- `/sync_events` - Синхронизирует события с Google Календарем.
- `/cancel` - Отменяет текущую операцию и возвращает в главное меню.

## Структура кода

### Основные компоненты

- **`bot.py`** - Основной файл, реализующий логику бота.
- **`commands/`** - Папка, содержащая различные команды:
  - `register.py` - Команды для работы с пользователями.
  - `meetings.py` - Управление встречами (создание, удаление, просмотр).
  - `stats.py` - Сбор и отображение статистики встреч.
  - `reminders.py` - Напоминания о встречах.
  - `help.py` - Функции, связанные с помощью и интерфейсом.
  - `utils.py` - Вспомогательные функции

- **`google_auth.py`** - Функции для аутентификации и работы с Google API.
- **`test_public.py`** - Тесты для функций
- **`test_database`** - Тестовая база данных