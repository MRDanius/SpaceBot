import telebot
from telebot import types
import random
import json
import requests
import threading
import time

API = 'db53663bae2e3b33d925fcb7279e77a2'
bot = telebot.TeleBot('7649584865:AAHMm0zIKXiODKCGu-jJ3fzZaJGCu6Fm2Jg')
user_data={}

# ==== ДОБАВЬ СЮДА СВОИ ГИФКИ, порядок должен совпадать с FACTS ====
GIFS = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa29paWhiajY3N29tNzdzbmtqMjU2ZXljNTFoeDhiaHprcHo3ZWo4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9tx0gy37p7oXu/giphy.gif", #change
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa29paWhiajY3N29tNzdzbmtqMjU2ZXljNTFoeDhiaHprcHo3ZWo4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPtjElfqwMOTbH2/giphy.gif", #change
    "https://media.giphy.com/media/l0IyjcSmE0QPTBhAs/giphy.gif?cid=ecf05e47s15e194c7cj8me5qxguyr0heh65m3463683fnuvx&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/GuFALVnrfpNhm/giphy.gif?cid=ecf05e47s15e194c7cj8me5qxguyr0heh65m3463683fnuvx&ep=v1_gifs_search&rid=giphy.gif&ct=g",   #change
    "https://media.giphy.com/media/5yaou1jFxTV6M/giphy.gif?cid=ecf05e47qbhek2j6f8zrs3s0yte3ievtdieythxajvimd2w0&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa29paWhiajY3N29tNzdzbmtqMjU2ZXljNTFoeDhiaHprcHo3ZWo4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/kiWlpxD6hXmvTL8dio/giphy.gif", #change
    "https://media.giphy.com/media/3o7TKCTt7cNHg10utO/giphy.gif?cid=ecf05e47thqlwawon4hlu7ubgy3spvunh9jm1yg4oj0tvt17&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/3o7TKWvwyGpgtlxQFq/giphy.gif?cid=ecf05e47jq7hdybgh8lqxc47plv2jvi4odvbsqo26zpeoqfh&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/yGgdwo7YfmrNS/giphy.gif?cid=ecf05e47azaamzq4t572pw3azy3yv20j5ni6n0pqy591rjvt&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/xT0BKEksASgc4OJGxy/giphy.gif?cid=ecf05e47azaamzq4t572pw3azy3yv20j5ni6n0pqy591rjvt&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/tdC6N1RKNp4swre2JY/giphy.gif?cid=ecf05e471rxcgd1ysmevnl9b3snefjv9fnev1sm75tjeh9de&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/GyJ8p0Um850ic/giphy.gif?cid=ecf05e471rxcgd1ysmevnl9b3snefjv9fnev1sm75tjeh9de&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/YRzQnWzbn4WIxd3ZYx/giphy.gif?cid=ecf05e471rxcgd1ysmevnl9b3snefjv9fnev1sm75tjeh9de&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/xT39CTrFW4nHLdBPpu/giphy.gif?cid=ecf05e474xc30tdvkk217rs46fk0fq7itfkh7aagyzda8ch7&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/SVCSsoKU5v6ZJLk07n/giphy.gif?cid=ecf05e474xc30tdvkk217rs46fk0fq7itfkh7aagyzda8ch7&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change
    "https://media.giphy.com/media/Tpkr2CSADfZwJUwTlD/giphy.gif?cid=ecf05e474ha9rtxful9cazzuvgl25bh8lxamtaz0gj8ohvly&ep=v1_gifs_search&rid=giphy.gif&ct=g", #change 
]
# ==== КОНЕЦ ДОБАВЛЕНИЯ ====

FACTS = [
    "🐕 **Собаки-космонавты Белка и Стрелка** (1960) стали первыми, кто вернулся из орбитального полёта живым. Стрелка позже родила здоровых щенков!", #yet
    "🚀 **Первый искусственный спутник** (1957) — «Спутник-1» весил всего 84 кг и передавал легендарные сигналы «бип-бип», которые ловили радиолюбители по всему миру.", #yet
    "🌕 **Тайна обратной стороны Луны** (1959) — Советская станция «Луна-3» впервые в истории сфотографировала невидимую с Земли сторону Луны, открыв миру совершенно новый ландшафт.",#yet
    "👨‍🚀 **108 минут, изменившие мир** (1961) — Полёт Гагарина длился меньше двух часов, но навсегда сделал СССР первопроходцем космоса. Его позывной «Кедр» знала вся планета!",#yet
    "🛰️ **Спутник-шпион с сюрпризом** (1960-е) — Советские аппараты «Зенит» возвращали капсулы с плёнкой, которые искали в тайге с вертолётов. Однажды медведи приняли капсулу за мёд и повредили её!", #yet
    "🌌 **Рекорд Венеры** (1970) — «Венера-7» совершила первую мягкую посадку на адской поверхности Венеры (465°C!) и передавала данные 23 минуты — подвиг инженерной мысли.", #yet
    "🔭 **Космический телескоп-невидимка** (1983) — «Астрон» с зеркалом 80 см стал крупнейшим ультрафиолетовым телескопом своего времени и открыл тысячи новых галактик.", #yet
    "🤖 **Автоматический космический челнок** (1988) — «Буран» совершил единственный полёт вообще без экипажа, в полностью автоматическом режиме — технология, до сих пор непревзойдённая на Западе.", #yet
    "👾 **Луноходы с характером** (1970-е) — Советские луноходы могли «просыпаться» по команде с Земли, грелись ядерным нагревателем и оставляли на Луне «автографы» — зеркала для лазерной локации.", #yet
    "🛰️ **Секретный двойник** (1970-е) — Каждый научный спутник серии «Космос» на деле мог быть военным, а их настоящие задачи рассекречивают только сейчас!", #yet
    "🌠 **Космическая станция-долгожитель** (1986-2001) — «Мир» проработала в 3 раза дольше запланированного срока и стала первым «космическим домом» для международных экипажей.", #yet
    "⚡ **Энергия ядра в космосе** (1960-е) — СССР запускал спутники с ядерными реакторами на борту. «Космос-1867» проработал на орбите целый год!",#yet
    "🧪 **Космическая алхимия** (1990-е) — На станции «Мир» выращивали идеальные кристаллы полупроводников, которые невозможно создать в земных условиях.", #yet
    "🛸 **Охота за НЛО** (1978) — Советские ВВС имели секретную инструкцию для пилотов по взаимодействию с «аномальными воздушными явлениями» — документ рассекретили в 2000-х.", #yet
    "🌑 **Лунные роботы-разведчики** (1970) — Перед отправкой луноходов СССР сбросил на Луну два «шагающих» аппарата ПрОП-М — они напоминали маленькие стиральные машины на лыжах!", #yet
    "🚀 **Ракета, опередившая время** (1960-е) — «Н-1» могла бы доставить советских космонавтов на Луну, но её двигатели (30 одновременно!) оказались слишком сложными для своей эпохи." #yet
]

# ==== ДОБАВЛЕНО: для контроля неповторяющихся фактов ====
sent_facts = {}
# ==== КОНЕЦ ДОБАВЛЕНИЯ ====

@bot.message_handler(commands=['start'])
def button_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Интересный факт 🚀")
    markup.add(btn1)
    btn2 = types.KeyboardButton("Узнать погоду за бортом")
    markup.add(btn2)
    btn3 = types.KeyboardButton("Сыграть в космическую викторину")
    markup.add(btn3)
    bot.send_message(message.chat.id, "Привет, космический исследователь! Я расскажу тебе о великих достижениях СССР в космосе. 🌌\n\n Выбери одну из кнопок снизу, которую ты хочешь", reply_markup = markup)

# ==== ИЗМЕНЕНО: теперь отправляется гифка + факт, без повторов пока не покажет все ====
@bot.message_handler(func=lambda message:message.text == 'Интересный факт 🚀')
def send_fact(message):
    user_id = message.from_user.id
    if user_id not in sent_facts or len(sent_facts[user_id]) == len(FACTS):
        sent_facts[user_id] = set()
    available = [i for i in range(len(FACTS)) if i not in sent_facts[user_id]]
    idx = random.choice(available)
    sent_facts[user_id].add(idx)
    fact = FACTS[idx]
    gif = GIFS[idx]
    bot.send_animation(message.chat.id, gif)
    bot.send_message(message.chat.id, f"📡 <b>Космический факт СССР:</b>\n\n{fact}", parse_mode="HTML")
# ==== КОНЕЦ ИЗМЕНЕНИЯ ====

@bot.message_handler(func=lambda message: message.text == "Узнать погоду за бортом")
def ask_city(message):
    bot.send_message(message.chat.id, "Введите название <b>города</b> мимо, которого мы пролетаем", parse_mode="HTML")
    bot.register_next_step_handler(message,send_weather)
def send_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f"Сейчас погода: {temp}℃")
    else:
        bot.reply_to(message, "Возможно, этот город находится не на Земле. Введите корректный город)")
        bot.register_next_step_handler(message, ask_city)

@bot.message_handler(func=lambda message:message.text == "Сыграть в космическую викторину")
def choose_tema(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_astronauts = types.KeyboardButton("Космонавты")
    btn_satellites = types.KeyboardButton("Спутники")
    btn_stations = types.KeyboardButton("Станции")
    btn_tech = types.KeyboardButton("Технологии")
    markup.add(btn_astronauts, btn_satellites, btn_stations, btn_tech)
    bot.send_message(message.chat.id, 'Выберите тему викторины', reply_markup=markup)

def load_questions(topic):
    with open(f"{topic}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        questions = data["questions"]
        return {
            "easy": questions[:6],
            "medium": questions[6:14],
            "hard": questions[14:]
        }

@bot.message_handler(func=lambda msg: msg.text in ["Космонавты", "Спутники", "Станции", "Технологии"])
def start_quiz(message):
    user_id = message.from_user.id
    topic = message.text.lower()
    user_data[user_id] = {
        "topic": topic,
        "score": 0,
        "questions": load_questions(topic),
        "current_question": None,
        "timer": None
    }
    ask_difficulty(message.chat.id, user_id)

def ask_difficulty(chat_id, user_id):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    easy_btn = types.KeyboardButton("🟢 Лёгкий")
    medium_btn = types.KeyboardButton("🟡 Средний")
    hard_btn = types.KeyboardButton("🔴 Сложный")
    markup.add(easy_btn, medium_btn, hard_btn)
    quit_btn = types.KeyboardButton("Завершить викторину")
    markup.add(quit_btn)
    questions_left = ""
    for diff, questions in user_data[user_id]["questions"].items():
        if questions:
            emoji = "🟢" if diff == "easy" else "🟡" if diff == "medium" else "🔴"
            questions_left += f"{emoji} {len(questions)} | "
    bot.send_message(chat_id,f"Выбери сложность следующего вопроса:\n(Осталось: {questions_left[:-2]})",reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text in ["🟢 Лёгкий", "🟡 Средний", "🔴 Сложный"])
def set_difficulty(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return choose_tema(message)
    difficulty_map = {
        "🟢 Лёгкий": "easy",
        "🟡 Средний": "medium",
        "🔴 Сложный": "hard"
    }
    difficulty = difficulty_map[message.text]
    if not user_data[user_id]["questions"][difficulty]:
        bot.send_message(message.chat.id, f"Вопросы уровня {message.text} закончились!")
        return ask_difficulty(message.chat.id, user_id)
    question = user_data[user_id]["questions"][difficulty].pop(0)
    user_data[user_id]["current_question"] = {
        "question": question,
        "difficulty": difficulty
    }
    send_question(message.chat.id, user_id)

def send_question(chat_id, user_id):
    question_data = user_data[user_id]["current_question"]
    question = question_data["question"]
    difficulty = question_data["difficulty"]
    options = question["options"]
    random.shuffle(options)
    markup = types.InlineKeyboardMarkup()
    row = []
    for i, option in enumerate(options):
        callback_data = f"ans_{i}_{option}"
        row.append(types.InlineKeyboardButton(option, callback_data=callback_data))
        if len(row) == 2:
            markup.row(*row)
            row = []
    if row:
        markup.row(*row)
    diff_emoji = "🟢" if difficulty == "easy" else "🟡" if difficulty == "medium" else "🔴"
    timer_seconds = 30
    msg = bot.send_message(
        chat_id,
        f"{diff_emoji} Вопрос ({difficulty.capitalize()}):\n\n{question['question']}\n\n⏳ Осталось: {timer_seconds} сек.",
        reply_markup=markup
    )
    user_data[user_id]["question_msg_id"] = msg.message_id
    user_data[user_id]["timer_seconds"] = timer_seconds
    user_data[user_id]["timer_cancel"] = False
    user_data[user_id]["timer_start"] = time.time()

    def update_timer():
        for sec in range(timer_seconds - 1, 0, -1):
            if user_id not in user_data or user_data[user_id].get("timer_cancel"):
                break
            next_tick = user_data[user_id]["timer_start"] + (timer_seconds - sec)
            sleep_time = max(0, next_tick - time.time())
            time.sleep(sleep_time)
            if user_id not in user_data or user_data[user_id].get("timer_cancel"):
                break
            try:
                bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=msg.message_id,
                    text=f"{diff_emoji} Вопрос ({difficulty.capitalize()}):\n\n{question['question']}\n\n⏳ Осталось: {sec} сек.",
                    reply_markup=markup
                )
            except:
                pass
            user_data[user_id]["timer_seconds"] = sec
    threading.Thread(target=update_timer, daemon=True).start()
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    timer = threading.Timer(timer_seconds, timeout_question, args=[chat_id, user_id])
    user_data[user_id]["timer"] = timer
    timer.start()

def timeout_question(chat_id, user_id):
    if user_id in user_data and not user_data[user_id].get("timer_cancel"):
        user_data[user_id]["timer_cancel"] = True
        question = user_data[user_id]["current_question"]["question"]
        bot.send_message(chat_id, f"⏰ Время вышло! Правильный ответ: {question['answer']}\n{question['explanation']}")
        ask_difficulty(chat_id, user_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("ans_"))
def handle_answer(call):
    user_id = call.from_user.id
    if user_id not in user_data:
        return
    user_data[user_id]["timer_cancel"] = True
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    parts = call.data.split("_")
    selected_idx = int(parts[1])
    selected_text = "_".join(parts[2:])
    question = user_data[user_id]["current_question"]["question"]
    difficulty = user_data[user_id]["current_question"]["difficulty"]
    if selected_text == question["answer"]:
        points = {"easy": 1, "medium": 3, "hard": 5}[difficulty]
        user_data[user_id]["score"] += points
        response = f"✅ Верно! +{points} баллов"
    else:
        response = f"❌ Неверно! Правильный ответ: {question['answer']}"
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"{call.message.text}\n\n{response}",
            reply_markup=None
        )
    except:
        pass
    bot.send_message(call.message.chat.id, f"📚 Пояснение:\n{question['explanation']}\n\nТвой счет: {user_data[user_id]['score']}")
    total_questions_left = sum(len(q) for q in user_data[user_id]["questions"].values())
    if total_questions_left == 0:
        finish_quiz(call.message.chat.id, user_id)
    else:
        ask_difficulty(call.message.chat.id, user_id)

@bot.message_handler(func=lambda msg: msg.text == "Завершить викторину")
def quit_quiz(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сейчас викторина не запущена. Нажмите 'Сыграть в космическую викторину', чтобы начать!")
        return
    user_data[user_id]["timer_cancel"] = True
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    finish_quiz(message.chat.id, user_id, manual=True)

def finish_quiz(chat_id, user_id, manual=False):
    score = user_data[user_id]["score"]
    topic = user_data[user_id]["topic"]
    if score >= 30:
        rank = "👨‍🚀 Генерал космических войск!"
    elif score >= 20:
        rank = "🛰️ Главный конструктор!"
    elif score >= 10:
        rank = "🚀 Космический инженер!"
    else:
        rank = "🌍 Начинающий исследователь!"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Интересный факт 🚀"))
    markup.add(types.KeyboardButton("Узнать погоду за бортом"))
    markup.add(types.KeyboardButton("Сыграть в космическую викторину"))
    if manual:
        bot.send_message(chat_id,
            f"🏁 Викторина завершена по вашему запросу!\n\n"
            f"Тема: {topic.capitalize()}\n"
            f"Набрано баллов: {score}\n"
            f"Твое звание: {rank}",reply_markup=markup
        )
    else:
        bot.send_message(chat_id,
            f"🏆 Викторина завершена!\n\n"
            f"Тема: {topic.capitalize()}\n"
            f"Набрано баллов: {score}\n"
            f"Твое звание: {rank}",reply_markup=markup
        )
    if user_id in user_data:
        del user_data[user_id]

bot.polling(none_stop=True)