# #ДЗУрок8 Дэдлайн 24.04.2022 23 59
# Создать программу “Таблица умножения”.
# Программа должна запрашивать у пользователя имя и количество попыток. Затем работать в бесконечном цикле до истечения указанных попыток.
# Программа должна запрашивать произведение двух случайных чисел от 1 до 9. После ввода пользователем ответа, выводить на экран правильный ответ.
# Каждый вопрос-ответ записывать в файл results.txt
# В этот же файл дописать итоговый отчёт с указанием имени, количества попыток и затраченного времени.
from random import randint
from datetime import datetime
import shelve

attempts = 0
answer = 0
random_number_1 = 0
random_number_2 = 0
start_game = datetime.now()
results = []

print("Tablica_umnozheniya_game.exe?")
name = input("Введите ваше имя: ")
print(f"Добро пожаловать {name} в Tablica_umnozheniya_game.exe?, это игра где надо решать таблицу умножения!!!")
attempts = int(input("Введите кол-во попыток для игры: "))
print("Игра началась!")

while True:
    try:
        random_number_1 = randint(1, 9)
        random_number_2 = randint(1, 9)
        answer = random_number_1 * random_number_2
        print(f" {answer}")
        print(f"У вас {attempts} попыток!")
        otveta = int(input(f"Сколько будет {random_number_1} * {random_number_2} = ?: "))
    except:
        print("Введите цифры, а не буквы!")
        continue
    if otveta < 1 or otveta > 100:
        print("Ответ не может быть ниже 1, и не может быть выше 100")
        continue
    if answer != otveta:
        print("Ответ неправильный!")
        print(f"У вас {attempts} попыток!")
        attempts -= 1
    else:
        print("Ответ правильный!")
    if attempts == 0:
        print("Вы исчерпали все ваши попытки!")
        end_game = datetime.now()
        print(f"Время игры: {start_game - end_game}")
        break


with open("results.txt", "a") as results:
    results.write(str(name))
    results.write("\n")
    results.write(str(random_number_1))
    results.write("*")
    results.write(str(random_number_2))
    results.write("=")
    results.write(str(answer))
    results.write(f"Время игры: {start_game - end_game}")
    results.write("\n")
    results.close()

