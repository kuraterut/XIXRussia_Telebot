import telebot
from telebot import types

bot = telebot.TeleBot("6711436501:AAETs68Uq75PucUpTSwwSbwpEOSR10uC6GU")
flag = 0
flag_name = ""
ruller_name = ""
STATES = []
#========================#
#Вопросы
#========================#
answer_count = 0
quest_num = 0
spis_question = []
spis_answer = []
spis_variants = []
file_questions = open("Викторина/Questions.txt", "r", encoding="utf-8")
data = file_questions.read().split("\n\n")
for i in range(len(data)):
    spis_answer.append(data[i].split("\n")[0][0])
    spis_question.append(data[i].split("\n")[0][1:])
    spis_variants.append(data[i].split("\n")[1:])
file_questions.close()
#========================#
#Правители
#========================#
file_ruller_list = open("Правители/Rullers_list.txt", "r", encoding="utf-8")
rullers_list = file_ruller_list.read().split("\n")
for i in range(len(rullers_list)):
    rullers_list[i] = rullers_list[i].split(")")[1]
file_ruller_list.close()


def variants_stroka(stroka):
    ans = ""
    for i in range(4):
        ans += stroka[i]
        ans += "\n"
    return ans


def window(message, bot_func):
    global flag, flag_name, quest_num, answer_count, spis_answer, spis_question, spis_variants, rullers_list, ruller_name, STATES
    btn_escape = types.KeyboardButton("Назад")
    btn_home = types.KeyboardButton("Домой")
    if flag == 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Викторина")
        btn2 = types.KeyboardButton("Источники")
        btn3 = types.KeyboardButton("Правители")
        btn4 = types.KeyboardButton("Выводы(Аналитика)")
        markup.add(btn1, btn2, btn3, btn4)
        bot_func.send_message(message.from_user.id, "Привет, я бот, который расскажет тебе про Россию времен 19 века.\n"
                                           "Выбери интересующий тебя вариант", reply_markup=markup)

    elif flag_name == "Назад":
        flag -= 2
        STATES.pop(-1)
        STATES.pop(-1)
        flag_name = STATES[-1]
        window(message, bot)

    elif flag_name == "Домой":
        flag = 0
        STATES = ["START"]
        window(message, bot)

    elif flag == 1 and flag_name == "Викторина":
        quest_num = 0
        answer_count = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать")
        markup.add(btn1, btn_escape)
        bot_func.send_message(message.from_user.id, "Готовы начать викторину?", reply_markup=markup)

    elif flag == 2 and flag_name == "Начать":
        answer_count = 0
        quest_num = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("A")
        btn2 = types.InlineKeyboardButton("B")
        btn3 = types.InlineKeyboardButton("C")
        btn4 = types.InlineKeyboardButton("D")
        markup.add(btn1, btn2, btn3, btn4)
        bot_func.send_message(message.from_user.id, spis_question[quest_num])
        bot_func.send_message(message.from_user.id, variants_stroka(spis_variants[quest_num]))
        bot_func.send_message(message.from_user.id, "Выберите вариант ответа", reply_markup=markup)
        quest_num += 1

    elif flag > 2 and flag_name in ["A", "B", "C", "D"]:
        if flag_name == spis_answer[quest_num - 1]:
            answer_count += 1
        if quest_num == len(spis_answer):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_home)
            bot_func.send_message(message.from_user.id, "Ваш результат: " + str(answer_count))
            bot_func.send_message(message.from_user.id, "Нажмите кнопку Домой, чтобы вернуться в главное меню", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardButton("A")
            btn2 = types.InlineKeyboardButton("B")
            btn3 = types.InlineKeyboardButton("C")
            btn4 = types.InlineKeyboardButton("D")
            markup.add(btn1, btn2, btn3, btn4)
            bot_func.send_message(message.from_user.id, spis_question[quest_num])
            bot_func.send_message(message.from_user.id, variants_stroka(spis_variants[quest_num]))
            bot_func.send_message(message.from_user.id, "Выберите вариант ответа", reply_markup=markup)
            quest_num += 1

    elif flag == 1 and flag_name == "Источники":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_escape)
        bot_func.send_message(message.from_user.id, "1)История России в датах с древнейших времен до наших дней : учебное пособие. — Москва : РГ-Пресс, 2019. — 560 с. [ил.]\n\n"
                                                    "2)https://arzamas.academy/themes/nineteenth\n\n"
                                                    "3)The Russian Empire and the National Periphery: Between the Theory of Autocracy and Management Practices ; Российская империя и национальные окраины: между теорией самодержавия и практикой управления. (2018). Retrieved from http://search.ebscohost.com/login.aspx?direct=true&site=eds-live&db=edsbas&AN=edsbas.20F2E271\n\n"
                                                    "4)Kondratiev, S. (2013). Отмена крепостного права. Реформа 1861 г. в современном официальном дискурсе и в оппозиционных дискурсах. Retrieved from http://search.ebscohost.com/login.aspx?direct=true&site=eds-live&db=edsbas&AN=edsbas.50C6BDEE\n\n"
                                                    "5)Учебник История России Орлов А.С. (с иллюстрациями) 3-е издание | Орлов А. С., Георгиев В. А. \n\n"
                                                    "6)Истории России XX – начала XXI века. / Под ред. Л. В. Милова. М.,\n\n"
                                                    "7)История России, XX век: Курс лекций / Под ред. В.В. Минаева. М.,\n\n"
                                                    "8)Кацва Л.А, Жукова Л.В. История России в датах: Справочник. М., 2013\n\n",
                                                    reply_markup=markup)

    elif flag == 1 and flag_name == "Правители":
        ruller_name = ""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_escape)
        bot_func.send_message(message.from_user.id, "Выберите правителя из списка:")
        file_rullers_list = open("Правители/Rullers_list.txt", "r", encoding="utf-8")
        bot_func.send_message(message.from_user.id, file_rullers_list.read())
        file_rullers_list.close()
        bot_func.send_message(message.from_user.id, "Напишите только число, под которым стоит желаемый правитель", reply_markup=markup)

    elif flag == 2 and flag_name in [str(x) for x in range(1, len(rullers_list)+1)]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_info = types.KeyboardButton("Информация")
        btn_opinion = types.KeyboardButton("Мнения")
        markup.add(btn_info, btn_opinion, btn_escape)
        ruller_name = rullers_list[int(flag_name)-1]
        bot_func.send_message(message.from_user.id, "Что вы хотите узнать об этом правителе("+ruller_name+")", reply_markup=markup)

    elif flag == 3 and flag_name == "Информация":
        file_ruller = open(f'Правители/{ruller_name}/Информация.txt', "r", encoding="utf-8")
        bot_func.send_message(message.from_user.id, file_ruller.read())
        file_ruller.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_want_opinion = types.KeyboardButton("Оставить мнение")
        markup.add(btn_want_opinion, btn_escape, btn_home)
        bot_func.send_message(message.from_user.id, "Хотите оставить свое мнение об этом правителе?", reply_markup=markup)

    elif flag == 3 and flag_name == "Мнения":
        file_ruller = open(f'Правители/{ruller_name}/Мнения.txt', "r", encoding="utf-8")
        bot_func.send_message(message.from_user.id, file_ruller.read())
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_escape, btn_home)
        bot_func.send_message(message.from_user.id, "Нажмите кнопку Домой или Назад", reply_markup=markup)

    elif flag == 4 and flag_name == "Оставить мнение":
        bot_func.send_message(message.from_user.id, "Напишите текст в формате:\nФИО(Аноним)\nСфера деятельности\nТекст мнения")

    elif flag == 5:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_home)
        f = open(f'Правители/{ruller_name}/Мнения.txt', "a", encoding="utf-8")
        f.write(flag_name+"\n\n")
        f.close()
        bot_func.send_message(message.from_user.id, "Спасибо за ваше мнение. Нажмите кнопку Домой", reply_markup=markup)

    elif flag == 1 and flag_name == "Выводы(Аналитика)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_escape)
        f = open("Выводы/Выводы.txt", "r", encoding="utf-8")
        bot_func.send_message(message.from_user.id, f.read(), reply_markup=markup)
        f.close()

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_escape)
        bot.send_message(message.from_user.id, "Я вас не понимаю", reply_markup=markup)
        flag -= 1


@bot.message_handler(commands=['start'])
def start(message):
    global flag, flag_name, STATES
    flag = 0
    STATES.append("START")
    flag_name = ""
    window(message, bot)
    flag += 1


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    global flag, flag_name

    flag_name = message.text
    STATES.append(flag_name)
    window(message, bot)
    flag += 1


bot.polling(none_stop=True, interval=0)