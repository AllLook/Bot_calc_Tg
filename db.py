import datetime
import telebot

time = datetime.datetime.now()


def in_log(message,command):
    file = open("log.csv", "a")
    file.write(f"{message.from_user.first_name},{message.from_user.id}, {time},{command[0]}\n")
    file.close()
