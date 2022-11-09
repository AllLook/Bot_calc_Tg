import random
import telebot  # библиотека для работы телеграм(лучше через venv)
from math import sqrt
from telebot import types
import options as op
import db

token = ""  # токен полученный от телеграм
bot = telebot.TeleBot(token)

# a = ""
# sig = ""
# b = ""
# result = ""


HELP = """
/help - вывести инфо
/sum - сложение
/pow - возведение в степень
/mult - умножение
/sub - разница
/div - деление
/rem - остаток от деления
/in_div - целочисленное деление
/root_num - квадратный корень
/complex_number - операции с комплексными числами,по аналогии со стандартными математическими операциями,но при этом числа преобразуются в комплексные
"""


@bot.message_handler(commands=["help"])  # регистрация команды и как она обработается(функциями)
def hello(message):
    if message.text == "/help":
        msg = bot.reply_to(message,
                           "Привет " + message.from_user.first_name + " Рад помочь, для работы с калькулятором вводите команды из меню через" + "  '/'  " + "и через пробел вводите элементы и знаки операций. Для помощи введите /help повторно")
        bot.register_next_step_handler(msg,
                                       hel)  # Вывод подсказки для пользователя и переход на следующий шаг в этом обработчикеы


def hel(message):
    bot.send_message(message.chat.id, HELP)  # Вывод инфо через созданную переменную


@bot.message_handler(commands=["sum"])
def addition(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message,command)
    if len(command) >= 3:
        a = float(command[1])  # значения в индексах превращаются в цифры
        b = float(command[3])
        sig = command[2]  # знак операции в строковом виде
        if sig == "+":  # если знак соответствует предполагаемой операции
            res = op.sum(a, b)  # выполнение соответствующей функции
            result = str(res)  # результат функции опять делаем строкой
        elif sig != "+":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)  # вывод для пользователя результата или сообщения об  ошибке
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["sub"])
def diff(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        a = float(command[1])
        b = float(command[3])
        sig = command[2]
        if sig == "-":
            res = op.sub(a, b)
            result = str(res)
        elif sig != "-":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["mult"])
def work(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        a = float(command[1])
        b = float(command[3])
        sig = command[2]
        if sig == "*":
            res = op.mult(a, b)
            result = str(res)
        elif sig != "*":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["pow"])
def degree(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        a = float(command[1])
        b = float(command[3])
        sig = command[2]
        if sig == "**":
            res = op.pow(a, b)
            result = str(res)
        elif sig != "**":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["div"])
def division(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        a = float(command[1])
        b = float(command[3])
        sig = command[2]
        if sig == "/" and b != 0:
            res = op.div(a, b)
            result = str(res)
        elif sig != "/":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["rem"])
def rem_division(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        a = float(command[1])
        b = float(command[3])
        sig = command[2]
        if sig == "%" and b != 0:
            res = op.rem_of_div(a, b)
            result = str(res)
        elif sig != "%":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["in_div"])
def int_division(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        a = float(command[1])
        b = float(command[3])
        sig = command[2]
        if sig == "//" and b != 0:
            res = op.int_div(a, b)
            result = str(res)
        elif sig != "//":
            result = "error"  # если пользователь ввел операцию от другой команды(не тот знак выражения)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["root_num"])
def root_numbers(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 1:
        a = float(command[1])
        res = sqrt(a)
        result = str(res)
        bot.send_message(message.chat.id, result)
    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


@bot.message_handler(commands=["complex_number"])
def com_num(message):
    mess = message.text.strip(' ')  # удаление лишних пробелов в начале и конце
    command = mess.split()  # сообщение от пользователя разбор на строковые элементы
    db.in_log(message, command)
    if len(command) >= 3:
        sig = command[2]
        a = float(command[1])
        a = complex(a)
        b = float(command[3])
        b = complex(b)
        if sig == "+":
            res = op.sum(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)
        elif sig == "-":
            res = op.sub(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)
        elif sig == "/":
            res = op.div(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)
        elif sig == "//":
            res = op.int_div(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)
        elif sig == "%":
            res = op.rem_of_div(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)
        elif sig == "**":
            res = op.pow(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)
        elif sig == "*":
            res = op.mult(a, b)
            result = str(res)
            bot.send_message(message.chat.id, result)


    else:
        correction = "Повторите попытку с корректным вводом"
        bot.send_message(message.chat.id, correction)


bot.polling(none_stop=True)
