ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, ten))
degree_of_square = list(map(lambda x: x ** 2, evens))
print(f"Все целые числа списка ten: {ten}")
print(f"Четные цисла списка ten: {list(evens)}")
print(f"Возведенные в степнь из списка evens: {list(degree_of_square)}")


def ten(the_word=ten):
    while 1:
        try:
            index = input("Введите индекс: ")
            if index == 'exit':
                print("Программа завершена!")
                break
            else:
                print(the_word[int(index)])
        except Exception:
            print(f"Индекс: от 0 до {len(the_word) - 1}")

ten()



