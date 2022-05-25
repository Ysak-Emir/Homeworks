from datetime import datetime
from random import randint

attempts = 1
results = []
start_game = datetime.now()
number = 0
random_number = 0

print("Game.exe, угадай число от 1 до 100 и получишь шаурму!!!!!!")

while True:
    try:
        random_number = randint(1, 100)
        print(random_number)
        print("Произошла генерация числа, теперь угадайте сгенерированное число.")
        if random_number > 50:
            print("Подсказка: число большое 50")
        elif random_number < 50:
            print("Подсказка: число меньше 50")
        print("Вы должны угадать число от 1 до 100.")
        number = int(input(f"Введите число: "))
    except:
        print("Введите цифры, а не буквы!")
        continue
    if number < 1 or number > 100:
        print("Ошибка! Вы должны ввести число от 1 до 100!")
        continue
    if random_number != number:
        print("К сажелению вы не угадали число, шаурма коту под хвост((")
        attempts += 1
    else:
        print("Вы угадали число!!! Вы сэкономили 140 баксов на шаурму!)))")
        print(f"Вы использовали {attempts} попыток.")
        end_game = datetime.now()
        print(f"Время игры: {start_game - end_game}")
        break

