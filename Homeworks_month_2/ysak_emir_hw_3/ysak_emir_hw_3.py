import keyboard


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self, value):
        self.__cpu = value

    @cpu.setter
    def cpu(self, value):
        self.__memory = value

    @property
    def memory(self, value):
        self.__memory = value

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self, cpu, memory):
        return f"Cpu: {cpu}, memory: {memory}"

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __eq__(self, other):
        return self.memory == other.memory

class Phone:

    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_cards_list, call_to_number):
        self.__call_to_number = call_to_number
        self.__sim_cards_list = sim_cards_list
        while True:
            sim_cards_list = int(input("Выберите сим-карту: "))
            if sim_cards_list == 1:
                print(f"Вы выбрали симкарту {sim_cards_list}")
                call_to_number = int(input("Введите номер телефона: "))
                if call_to_number == str:
                    print("Номер телефона может быть только числовым!")
                    continue
                print(f"Вы позвонили на номер: {call_to_number}, с сим-карты: {sim_cards_list}")
            elif sim_cards_list > 1:
                print("У вас только 1 сим-карты!")
                continue
            else:
                print("Вы ввели неккоректные символы!")

    def __str__(self):
        super(Phone, self).__str__(f"Sim_card: {self.sim_cards_list}")


class SmartPhone(Computer, Phone):

    def __init__(self, location, cpu, memory):
        super().__init__(cpu, memory)
        self.location = location

    def use_gps(self, location):
        self.location = location
        while True:
            print("Включен GPS.")
            location = input("Куда вы хотите проложить маршрут?: ")
            if len(location) > 50:
                print("Максимум ввод символов 50!")
                continue
            elif len(location) < 3:
                print("Минимальный ввод символов 3!")
                continue
            elif location == "quit":
                print("Вы завершили программу GPS.")
                break
            else:
                print(f"Вы проложили на {location} маршрут.")


    def __str__(self):
        return super(SmartPhone, self).__str__(f"Location: {self.location}") + f"Cpu: {self.cpu}, " \
                                                                               f"Memory: {self.memory}" \
                                                                               f"Sim_card: {self.sim_cards_list}"


my_comp = Computer(4, 8096)
my_phone = Phone("MegaCom")
my_smartphone = SmartPhone("Bishkek", 8, 4096)
my_smartphone2 = SmartPhone("Kara-Balta", 6, 3072)
# my_smartphone.use_gps("Bishkek")
# my_phone.call("MegaCom", 0)
