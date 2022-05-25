print("Вас приветствует мастер список Менторов, здесь вы сможете добавить/изменить/удалить.")
mentors_word = 0
mentors_list = []
while True:
    menu = input(
        "Это ваше меню. Выберите одно из значений: \n1) Добавление, \n2) Изменение, \n3) Удаление, \n0) Выход \n: ")
    if menu == '1':
        print("Вы выбрали 'Добавление'.")
        men1 = input("Введите имя первого ментора: ")
        if len(men1) > 15:
            print("Имя должно содержать не больше 15 символов!")
        else:
            mentors_word = mentors_word + 1
            print(f"Добавлен в список: {men1.capitalize()}, {mentors_word} Ментор")
            mentors_list.append(men1.capitalize())

        men2 = input("Введите имя второго Ментора: ")
        if len(men2) > 15:
            print("Имя должно содержать не больше 15 символов!")
        else:
            mentors_word = mentors_word + 1
            print(f"Добавлен в список: {men2.capitalize()}, {mentors_word} Ментор")
            mentors_list.append(men2.capitalize())

        men3 = input("Введите имя тертьего Ментора: ")
        if len(men1) > 15:
            print("Имя должно содержать не больше 15 символов!")
        else:
            mentors_word = mentors_word + 1
            print(f"Добавлен в список: {men3.capitalize()}, {mentors_word} Ментор")
            mentors_list.append(men3.capitalize())

        men4 = input("Введите имя четвертого Ментора: ")
        if len(men1) > 15:
            print("Имя должно содержать не больше 15 символов!")
        else:
            mentors_word = mentors_word + 1
            print(f"Добавлен в список: {men4.capitalize()}, {mentors_word} Ментор")
            mentors_list.append(men4.capitalize())

        men5 = input("Введите имя пятого Ментора: ")
        if len(men5) > 15:
            print("Имя должно содержать не больше 15 символов!")
        else:
            mentors_word = mentors_word + 1
            print(f"Добавлен в список: {men5.capitalize()}, {mentors_word} Ментор")
            mentors_list.append(men5.capitalize())

        print(f"Добавлены {mentors_word} Ментора: {mentors_list} ")

    if menu == '2':
        print("Вы выбрали 'Изменение'")
        change1 = input("Введите имя Ментора которого хотите заменить: ")
        if change1 not in mentors_list:
            print("Этого Ментора нету в списке")
        else:
            print(f"Ментор {change1} Удален")
            mentors_list.pop(0)
            men1 = input("Введите новое имя ментора: ")
            if len(men1) > 15:
                print("Имя должно содержать не больше 15 символов!")
            else:
                mentors_word = mentors_word + 1
                print(f"Добавлен в список: {men1.capitalize()}, {mentors_word} Ментор")
                mentors_list.append(men1.capitalize())
                mentors_list.append(men1)
                print(f"Ментор {men1} добавлен")

    if menu == '3':
        del_men = input("Введите имя Ментора которого хотите удалить: ")
        if mentors_list is not mentors_list:
            print("Этого Ментора нету в списке")
        else:
            print(f"Ментор {del_men} Удален")
            mentors_list.pop(0)

    if menu == '0':
        new_mentors_list = tuple(mentors_list)
        print(f"Список Менторов: {new_mentors_list}")
        print("Программа завершена!")
        break








