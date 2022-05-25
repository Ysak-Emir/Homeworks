movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Морбиус": {}
}


def print_movies(movies=None):
    for key_film, value_rating in movies.items():
        movies = {
        "Django Unchained": {
            "John": 10,
            "Jack": 9
        },
        "Морбиус": {}
    }


def print_movies():
    for key_film, value_rating in movies.items():
        print(f"\nФильм: {key_film}")
        if len(value_rating) == 0:
            print("Рейтинг пока что не доступен.")
        else:
            print("Рейтинг:")
            for user, rate in value_rating.items():
                print(f"{user}: {value_rating}")


def add_film(film):
    if film in movies.keys():
        print("Этот фильм уже есть в списке!")
    else:
        movies.update({film: dict()})
        print("Вы успешно добавили фильм!")


def add_rating(film: object) -> object:
    if film not in movies.keys():
        print("Этого фильма нет в списке!")
    else:
        key_film = input("Введите ваше имя: ")
        value_rating = float(input("Укажите рейтинг к фильму: "))
        if 0 < value_rating <= 10:
            movies[film].update({key_film: value_rating})
            print(f"Рейтинг успешно добавлен к: {key_film} оценен: {value_rating}")
        else:
            print("Рейтинг должен быть от 1 до 10!")


def rating_view():
    for key_film, value_rating in movies.items():
        value_ratings = []
        for i in value_rating.values():
            value_ratings.append(i)
        if len(value_ratings) == 0:
            print(f"Рейтинг не доступен для: {key_film}")
        else:
            print(f"{key_film} оценивается {sum(value_ratings) / len(value_ratings)}")


while True:
    print_movies()
    menu = input("\nМеню: \n1) Добавить фильм \n2) Добавить рейтинг \n3) Посмотреть словарь \n4) Выход \n: ")
    if menu == '4':
        print("Программа завершена!")
        break
    elif menu == '1':
        print("Вы выбрали режим 'Добавить фильм.'. Введите название фильма которого хотите добавить.")
        film = input("Введите название фильма: ")
        add_film(film.capitalize())
    elif menu == '2':
        print("Вы выбрали режим 'Добавить рейтинг'. Введите название фильма и укажите рейтинг.")
        film = input("Введите название фильма: ")
        add_rating(film.capitalize())
    elif menu == '3':
        print("Вы выбрали режим 'Посмотреть словарь'.")
        rating_view()
    else:
        print("Данной операции не существует!")
        if len(rates) == 0:
            print("Рейтинга нет.")
        else:
            print("Рейтинг: ")
            for user, rates in rates.items():
                print(f"{user}: {rates}")
