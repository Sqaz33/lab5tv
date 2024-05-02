import matplotlib.pyplot as plt
from prettytable import PrettyTable


class Calculator:
    #------------математические методы---------------
    def get_frequencies(self, data: list[float]) -> list[int]:
        """
        Получить частоты
        :param data: статистические данные
        :return: частоты
        """
        count = dict()
        for i in data:
            count[i] = count.get(i, 0) + 1
        freq = []
        for i in sorted(count.keys()):
            freq.append(count[i])
        return freq

    def get_relative_frequencies(self, data: list[float]) -> list[float]:
        """
        Получить относительные частоты
        :param data: статистические данные
        :return: относительные частоты
        """
        freq = self.get_frequencies(data)
        return [i / sum(freq) for i in freq]

    #-------------решения задач-------------------------
    def solveB1(self, data: list[float]) -> list[float]:
        """
        Решить задачу B1:
        составить вариационный ряд
        :param data: статистические данные
        :return: вариацонный ряд
        """
        return list(sorted(set(data)))

    def solveC1(self, data: list[float]) -> tuple[PrettyTable, PrettyTable]:
        """
        Решить задачу С1:
        составить статистический ряд частот и ряд отностительных частот;
        построить график для каждого ряда
        :param data: статистические данные
        :return: статистические ряды, (неявно возвращается график plt.show())
        """
        freq = self.get_frequencies(data)
        relative_freq = self.get_relative_frequencies(data)

        var = self.solveB1(data)
        # Построение графиков
        fig1, pol1 = plt.subplots()
        fig1, pol2 = plt.subplots()

        pol1.plot(var, freq)
        pol1.set_title("Полигон частот")

        pol2.plot(var, relative_freq)
        pol2.set_title("Полигон относительных частот")

        # Построение таблиц
        freq_table = PrettyTable()
        freq_table.add_column("Xi", var)
        freq_table.add_column("Ni", freq)

        relative_freq_table = PrettyTable()
        relative_freq_table.add_column("Xi", var)
        relative_freq_table.add_column("Wi", [f'{i:.3f}' for i in relative_freq])

        return freq_table, relative_freq_table

    # def solveC2(self, data: list[float]) -> tuple(list[float], list[float], graph):
    def solveD1(self, data: list[float]) -> tuple[str, list[str]]:
        """
        Решить задачу D1:
        Дать определение функции распределения;
        Найти функцию распрееделения;
        Построить график для функции.
        :param data: статистические данные
        :return: определение фукнции, функцию распределения, (неявно возвращается график plt.show())
        """

        func_definition = ("Эмпирической функцией распредления называют функцию F*(x), определяющую для каждого значения x "
                           "относительну частоту события X < x: F*(x) = n_x/n")

        # получение ф-ции распр.
        X = self.solveB1(data)
        P = self.get_relative_frequencies(data)
        p = 0
        Fx = [0] + [p := p + i for i in P]

        # получение интервалов, для значения ф-ции распр.
        intervals = [(X[0]-10, X[0])]
        for i in range(0, len(X) - 1):
            intervals.append((X[i], X[i+1]))
        intervals += [(X[-1], X[-1] + 10)]
        
        # построение графика
        plt.xlim(intervals[0][0], intervals[-1][1])
        plt.ylim(0, 1.1)
        plt.title("Империческая функция распределения")
            # добавление стрелок     (xy)<------------(xytext)
        for i in range(len(Fx)):
            plt.annotate(
                '', xy=(intervals[i][0], Fx[i]), xytext=(intervals[i][1], Fx[i]),
                arrowprops=dict(width=0.01, headwidth=5)
                )
        
        # получаем строковое представленние функции
        str_intervals = ([f'x <= {X[0]}'] 
                         + [f'{i[0]} < x <= {i[1]}' for i in intervals[1:len(intervals)-1]]
                         + [f'x > {X[-1]}'])
        str_Fx = [f'если {xs} то F*(x) = {p}' for p, xs in zip([f'{p:0.3f}' for p in Fx], str_intervals)]

        return func_definition, str_Fx

    # def solveD2:
    # def solveE1::
    # def solveE2:


if __name__ == "__main__":
    calc = Calculator()
    data = [1, 4, 4, 6, 6, 16]
    # print(calc.solveC1(data))
    # ans = calc.solveD1(data)
    # print(ans[0])
    # for s in ans[1]:
    #     print(s)



    # # Отображение точки данных
    # plt.scatter(0.5, 0.5)

    # # Добавление аннотации с текстом и стрелкой
    # plt.annotate('', xy=(0.8, 0.5), xytext=(0.6, 0.6),
    #             arrowprops=dict(width=0.01, headwidth=5))

    # # Настройка границ графика
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)

    # Отображение графика
    ans = calc.solveD1(data)
    print(ans[0])
    for s in ans[1]:
        print(s)
    plt.show()



