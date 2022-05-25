print("Вас приветствует мастер вычисления слов! \nДля того чтобы диагнозировать слово, вы должны ввести слово...")
while True:
    word = input("Введите слово (quit) : ")
    if word == "quit":
        print("Вы завершили приложение!")
        break
    count = 0
    list1 = "ауоыиэяюёеaeiouАУОЫИЭЯЁЕAEIOU"
    for i in word:
        if i in list1:
            count = count + 1
    count1 = 0
    list2 = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyzБВГДЖЭЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPRSTVWYZ"
    for i in word:
        if i in list2:
            count1 = count1 + 1
    count3 = 0
    for i in word:
        if i in list1 or list2:
            count3 = count3 + 1
    print(f"Слово: {word}")
    print(f"количество букв: {count3}")
    print(f"гласные буквы: {count}")
    print(f"согласные буквы: {count1}")
    print(f'Гласные: {round(count / len(word) * 100, 2)}%'"\n"f'Согласные: {round(count1 / len(word) * 100, 2)}%')





