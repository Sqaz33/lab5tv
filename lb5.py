from calculator import Calculator
from generator import Generator

import os
import sys
from enum import Enum

import matplotlib.pyplot as plt


class Commands(Enum):
    B1 = "b1"
    C1 = "c1"
    D1 = "d1"
    E1 = "e1"
    B2 = "b2"
    C2 = "c2"
    D2 = "d2"
    E2 = "e2"
    FROM_FILE = "from_file"
    FROM_K = "from_k"
    DATA = "data"
    EXIT = "exit"
    HELP = "help"
    GEN = "gen"
    INTERV = "interv"
    CLEAR_INTERV = "clear_interv"


def com_contains_str_com(com: str) -> bool:
    return com in (c.value for c in Commands)


def get_data_from_file(path: str) -> list[...]:
    with open(path, 'r') as file:
        str_data = file.read().replace(' ', '').replace('\n', '')
        return [float(n) for n in str_data.split(';')]


def write_data_to_file(data: list[...]) -> str:
    with open("gen_data.txt", 'w') as file:
        file.write('; '.join(map(data, data)))
    path = os.path.abspath(sys.argv[0])
    return path[0: path.rfind('\\')]


def check_data(data: list[...], interv_data: list[...]) -> bool:
    if data is None and interv_data is None:
        print("Статистические данные не введены.")
        return False
    return True


if __name__ == "__main__":
    interv = "10;12 12;13 13;14"
    pass



if __name__ == "__main__":
    print("------------------------------------------\n"
          "Программа решение лабораторной работы №5.\n"
          "Разработчики: Рыжков М.М, Матвеев С.А.\n"
          "Группа: ПрИн-268.\n"
          "Волгоград 2024.\n"
          "-----------------------------------------\n"
          "Введите help, чтобы узнать полный список команд для работы\n")
    calc = Calculator()
    data = None
    interv_data: list[list[list[float]], list[int], list[float]] = None
    while True:
        com = input("Введите команду\n")
        com = com.replace(' ', '')
        command = Commands(com) if com_contains_str_com(com) else None

        match command:
            case Commands.B1:
                if check_data(data):
                    print("______решение B1______")
                    print(calc.solveB1(data))
                    print("----------------------")
            case Commands.C1:
                if check_data(data):
                    print("______решение C1______")
                    for t in calc.solveC1(data):
                        print(t)
                    print("----------------------")
                    plt.show()
            case Commands.D1:
                if check_data(data):
                    print("______решение D1______")
                    ans = calc.solveD1(data)
                    print(ans[0])
                    for f in ans[1]:
                        print(f)
                    print("----------------------")
                    plt.show()
            case Commands.E1:
                if check_data(data):
                    print("______решение E1______")
                    for i in calc.solveE1(data):
                        print(i)
                    print("----------------------")
            case Commands.B2:
                if check_data(data, interv_data):
                    print("______решение B2______")
                    if interv_data is None:
                        interval_number = int(input("Введите количество интервалов.\n"))
                        assert intervals > 0, "Количество интервалов должно быть > 0."
                        intervals = Calculator().get_intervals(data, interval_number)
                        freq = Calculator().get_intervals_frequencies(data, interval_number)
                        rel_freq = Calculator().get_intervals_relative_frequencies(data, interval_number)
                    else:
                        intervals = interv_data[0]
                        freq = interv_data[1]
                        rel_freq = interv_data[2]
                    print(calc.solveB2(intervals, freq, rel_freq))
                    print("----------------------")
                    plt.show()
            case Commands.C2:
                if check_data(data, interv_data):
                    print("______решение C2______")
                    if interv_data is None:
                        interval_number = int(input("Введите количество интервалов.\n"))
                        assert intervals > 0, "Количество интервалов должно быть > 0."
                        intervals = Calculator().get_intervals(data, interval_number)
                        freq = Calculator().get_intervals_frequencies(data, interval_number)
                        rel_freq = Calculator().get_intervals_relative_frequencies(data, interval_number)
                    else:
                        intervals = interv_data[0]
                        freq = interv_data[1]
                        rel_freq = interv_data[2]
                    print(calc.solveC2(intervals, freq, rel_freq))
                    print("----------------------")
                    plt.show()
            case Commands.D2:
                if check_data(data, interv_data):
                    print("______решение D2______")
                    if interv_data is None:
                        interval_number = int(input("Введите количество интервалов.\n"))
                        assert intervals > 0, "Количество интервалов должно быть > 0."
                        intervals = Calculator().get_intervals(data, interval_number)
                        freq = Calculator().get_intervals_frequencies(data, interval_number)
                        rel_freq = Calculator().get_intervals_relative_frequencies(data, interval_number)
                    else:
                        intervals = interv_data[0]
                        freq = interv_data[1]
                        rel_freq = interv_data[2]
                    res = calc.solveD2(intervals, freq, rel_freq)
                    print("__Эмпирическая функция распределения для интервального ряда__")
                    for s in res[0]:
                        print(s)
                    print("----------------------")
                    print("Эмпирическая функция распределения для группированного ряда")
                    for s in res[1]:
                        print(s)
                    print("----------------------")
                    plt.show()
            case Commands.E2:
                if check_data(data, interv_data):
                    print("______решение E2______")
                    if interv_data is None:
                        interval_number = int(input("Введите количество интервалов.\n"))
                        assert intervals > 0, "Количество интервалов должно быть > 0."
                        intervals = Calculator().get_intervals(data, interval_number)
                        freq = Calculator().get_intervals_frequencies(data, interval_number)
                        rel_freq = Calculator().get_intervals_relative_frequencies(data, interval_number)
                    else:
                        intervals = interv_data[0]
                        freq = interv_data[1]
                        rel_freq = interv_data[2]
                    for i in calc.solveE2(intervals, freq):
                        print(i)
                    print("----------------------")
            case Commands.FROM_FILE:
                path = input("Введите путь до файла.\n")
                try:
                    data = get_data_from_file(path)
                except Exception:
                    print("Невозможно прочитать файл.")
                    data = None
            case Commands.FROM_K:
                str_data = input("Введите статистические данные.\n")
                str_data = str_data.replace(' ', '').split(';')
                str_data = [n.replace(',', '.') for n in str_data]
                data = list(map(float, str_data))
            case Commands.DATA:
                if check_data(data, interv_data):
                    if not data is NULL:
                        print(data)
                    if not interv_data is NULL:
                        print(interv_data)
            case Commands.HELP:
                print(
                    "Список команд:\n"
                    "help - получить интрукцию к программе.\n"
                    "b1 - решить пункт b) задания 1.\n"
                    "c1 - решить пункт c) задания 1.\n"
                    "d1 - решить пункт d) задания 1.\n"
                    "e1 - решить пункт e) задания 1.\n"
                    "b2 - решить пункт b) задания 2.\n"
                    "c2 - решить пункт c) задания 2.\n"
                    "d2 - решить пункт d) задания 2.\n"
                    "e2 - решить пункт e) задания 2.\n"
                    "ВНИМАНИЕ: решение происходит только после загрузки данных из файла.\n"
                    "from_file - загрузить статистические данные из txt-файла.\n"
                    "from_k - ввести данные с клавиатуры.\n"
                    "data - введенные в программу статисические данные.\n"
                    "gen - сгенерировать файл случайных чисел.\n"
                    "exit - завершить работу программы.\n"
                )
            case Commands.GEN:
                gen_data = Generator.generate_list_of_number(
                    80, values=(-100, 100), freq=(10, 20)
                )
                print(f"Файл случайных чиселв сгенерирован в папке {write_data_to_file(gen_data)}.")
            case Commands.INTERV:
                str_interv = input("Введите интервалы.\n")
                str_freq = input("Введите частоты.\n")

                interv = str_interv.split(' ')
                interv = [s.split(';') for s in interv]
                interv = list(map(lambda i:[float(i[0]), float(i[1])], interv))

                freq = list(map(int, str_freq.split(' ')))
                rel_freq = [n / sum(freq) for n in freq]
                interv_data = [interv, freq, rel_freq]
            case Commands.CLEAR_INTERV:
                interv_data = None

            case Commands.EXIT:
                print("Программа прекращает работу.")
                break
            case _:
                print("Команда не распознана")
