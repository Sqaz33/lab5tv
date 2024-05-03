from calculator import Calculator
from generator import Generator

import os
import sys
from enum import Enum


class Commands(Enum):
    B1 = "b1"
    C1 = "c1"
    D1 = "d1"
    E1 = "e1"
    B2 = "b2"
    C2 = "c2"
    D2 = "d2"
    E2 = "e2"
    FROM_FILE = "load_data"
    EXIT = "exit"
    HELP = "help"
    GEN = "gen"


def com_contains_str_com(com: str) -> bool:
    return com in (c.value for c in Commands)


def get_data_from_file(path: str) -> list[...]:
    with open(path, 'r') as file:
        str_data = file.read().replace(' ', '').replace('\n', '')
        return [int(n) for n in str_data.split(',')]


def check_data(data: list[...]) -> bool:
    if data is None:
        print("Файл не загружен")
        return False
    return True


if __name__ == "__main__":
    print("------------------------------------------\n"
          "Программа решение лабораторной работы №5.\n"
          "Разработчики: Рыжков М.М, Матвеев С.А.\n"
          "Группа: ПрИн-268.\n"
          "Волгоград 2024.\n"
          "-----------------------------------------")
    calc = Calculator()
    while True:
        com = input("Введите команду\n")
        com = com.replace(' ', '')
        command = Commands(com) if com_contains_str_com(com) else None
        data = [1, 1, 5, 3, 7, 1, 3]

        match command:
            case Commands.B1:
                if check_data(data):
                    print("решение B1")
                    print(calc.solveB1(data))
            case Commands.FROM_FILE:
                path = input("Введите путь до файла.")
                try:
                    data = get_data_from_file(path)
                except Exception:
                    print("Невозможно прочитать файл")
                    data = None
            case Commands.HELP:
                print(
                    "Список команд:\n"
                    "help - получить интрукцию к программе\n"
                    "b1 - решить пункт b) задания 1\n"
                    "c1 - решить пункт c) задания 1\n"
                    "d1 - решить пункт d) задания 1\n"
                    "e1 - решить пункт e) задания 1\n"
                    "b2 - решить пункт b) задания 2\n"  
                    "c2 - решить пункт c) задания 2\n"
                    "d2 - решить пункт d) задания 2\n"
                    "e2 - решить пункт e) задания 2\n"
                    "ВНИМАНИЕ: решение происходит только после загрузки данных из файла\n"
                    "load_data - загрузить статистические данные из файла\n"
                    "gen - сгенерировать файл случайных чисел\n"
                    "exit - завершить работу программы\n"
                )
            case Commands.GEN:
                gen_data = Generator.generate_list_of_number(
                    80, values=(-100, 100), freq=(10, 20)
                )
                with open("gen_data.txt", 'w') as file:
                    file.write(', '.join(map(str, gen_data)))
                path = os.path.abspath(sys.argv[0])
                print(f"Файл случайных чиселв сгенерирован в папке {path[0: path.rfind('\\')]}")
            case Commands.EXIT:
                print("Программа прекращает работу.")
                break
            case _:
                print("Команда не распознана")
