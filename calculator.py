import matplotlib.pyplot as plt
from prettytable import PrettyTable

from math import ceil
from math import isclose


class Calculator:
    def __init__(self):
        self._sample_mean = """ 
        ___
        x_в = n^(-1) * sum(x_i * n_i) 
        """
        self._dispersion = """
              _____    ___
        D_в = x^2_в - (x_в)^2 
        """
        self._standard_deviation = """
        b = (D_в)^(0.5)
        """
        self._unbiased_assessment = """
        S = (n/(n - 1) * D_в)^(0.5)        
        """

    # ------------математичесие методы---------------
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

    def sample_mean(self, variation_series: list[float], frequencies: list[int]) -> float:
        """
        Получить выборочное среднее
        :param variation_series: вариационный ряд
        :param frequencies: ряд частот
        :return: выборочное среднее
        """
        return (1 / sum(frequencies)) * sum(x * n for x, n in zip(variation_series, frequencies))

    def dispersion(self, variation_series: list[float], frequencies: list[int]) -> float:
        """
        Получить дисперсию
        :param variation_series: выриационный ряд
        :param frequencies: ряд частот
        :return: дисперсия
        """
        x = self.sample_mean(variation_series, frequencies)
        x_2 = self.sample_mean([i ** 2 for i in variation_series], frequencies)
        return x_2 - x ** 2

    def standard_deviation(self, variation_series: list[float], frequencies: list[int]) -> float:
        """
        Получить квадратичное отклонение
        :param variation_series: выриационный ряд
        :param frequencies: ряд частот
        :return: квадратичное отклоненение
        """
        return self.dispersion(variation_series, frequencies) ** 0.5

    def unbiased_assessment(self, variation_series: list[float], frequencies: list[int]) -> float:
        """
        Получить несмещенную оценку
        :param variation_series: выриационный ряд
        :param frequencies: ряд частот
        :return: несмещенная оценка
        """
        n = sum(frequencies)
        return (n / (n - 1) * self.dispersion(variation_series, frequencies))**0.5

    def get_intervals(self, data: list[float], interval_number: int) -> list[list[int]]:
        var = self.solveB1(data)
        mx = max(var)
        mn = min(var)
        step = (mx - mn) / interval_number
        intervals = []
        x = mn
        while x + step <= mx:
            intervals.append([x, x := x + step])
        if not isclose(mx, intervals[-1][1], rel_tol=1e-9):
            intervals.append([mx - step, mx])
        return intervals

    def get_intervals_frequencies(self, data: list[float], interval_number: int) -> list[int]:
        var = self.solveB1(data)
        var_freq = self.get_frequencies(data)
        intervals = self.get_intervals(data, interval_number)
        freq = [0] * interval_number
        for i in range(interval_number):
            for j in range(len(var)):
                if intervals[i][0] <= var[j] < intervals[i][1]:
                    freq[i] += var_freq[j]
        for i in range(len(var)):
            if var[i] == intervals[-1][1]:
                freq[-1] += var_freq[i]
        # TODO: сделать проверку крайне правого значения
        return freq

    def get_intervals_relative_frequencies(self, data: list[float], interval_number: int) -> list[float]:
        var = self.solveB1(data)
        var_rel_freq = self.get_relative_frequencies(data)
        intervals = self.get_intervals(data, interval_number)
        rel_freq = [0] * interval_number
        for i in range(interval_number):
            for j in range(len(var)):
                if intervals[i][0] <= var[j] < intervals[i][1]:
                    rel_freq[i] += var_rel_freq[j]
        rel_freq[-1] += var_rel_freq[var.index(max(var))]
        return rel_freq

    def sublot_empirical_distribution_func(self, data: list[float], relative_frequencies: list[float], titel: str):
        # получение ф-ции распр.
        X = data
        P = relative_frequencies
        p = 0
        Fx = [0] + [p := p + i for i in P]

        # получение интервалов, для значения ф-ции распр.
        intervals = [(X[0] - 1, X[0])]
        for i in range(0, len(X) - 1):
            intervals.append((X[i], X[i + 1]))
        intervals += [(X[-1], X[-1] + 1)]

        # построение графика
        fig, graph = plt.subplots()
        graph.set_xlim(intervals[0][0], intervals[-1][1])
        graph.set_ylim(0, 1.1)
        graph.set_title(titel)
        # добавление стрелок     (xy)<------------(xytext)
        for i in range(len(Fx)):
            graph.annotate(
                '', xy=(intervals[i][0], Fx[i]), xytext=(intervals[i][1], Fx[i]),
                arrowprops=dict(width=0.01, headwidth=5)
            )
            # добавление пунктира
        for i in range(len(Fx) - 1):
            graph.plot(
                [intervals[i][1], intervals[i][1]], [0, Fx[i + 1]], linestyle="--", color="black"
            )

    # -------------решения задания 1-------------------------
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
        # получение частот и вар. ряда
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

    def solveD1(self, data: list[float]) -> tuple[str, list[str]]:
        """
        Решить задачу D1:
        Дать определение функции распределения;
        Найти функцию распрееделения;
        Построить график для функции.
        :param data: статистические данные
        :return: определение фукнции, функцию распределения, (неявно возвращается график plt.show())
        """

        func_definition = (
            "Эмпирической функцией распредления называют функцию F*(x), определяющую для каждого значения x "
            "относительну частоту события X < x: F*(x) = n_x/n"
        )

        # получение ф-ции распр.
        X = self.solveB1(data)
        P = self.get_relative_frequencies(data)
        p = 0
        Fx = [0] + [p := p + i for i in P]

        self.sublot_empirical_distribution_func(X, P, "Эмпирическая функция распределения")

        # получение интервалов, для значения ф-ции распр.
        intervals = [(X[0] - 1, X[0])]
        for i in range(0, len(X) - 1):
            intervals.append((X[i], X[i + 1]))
        intervals += [(X[-1], X[-1] + 1)]
        # получаем строковое представленние функции
        str_intervals = ([f'x <= {X[0]}']
                         + [f'{i[0]} < x <= {i[1]}' for i in intervals[1:-1]]
                         + [f'x > {X[-1]}'])
        str_Fx = [f'если {xs} то F*(x) = {p}' for p, xs in zip([f'{p:0.3f}' for p in Fx], str_intervals)]

        return func_definition, str_Fx

    def solveE1(self, data: list[float]) -> tuple[str, float, str, float, str, float, str, float]:
        """
        Решить задачу E1:
        Дать определение числовым характеристикам,
        получить эти числовые характеристики
        :param data: статистические данные
        :return: определение числовых характеристик,
        числовые характеристики
        """
        X = self.solveB1(data)
        N = self.get_frequencies(data)
        return (
            self._sample_mean,
            self.sample_mean(X, N),
            self._dispersion,
            self.dispersion(X, N),
            self._standard_deviation,
            self.standard_deviation(X, N),
            self._unbiased_assessment,
            self.unbiased_assessment(X, N)
        )

    # -------------решения задания 2-------------------------
    def solveB2(self, intervals: list[list[int]], freq: list[int], rel_freq: list[float]) -> PrettyTable:
        """
        Решить задачу В2
        получить интервальный ряда чатот и интервальный ряд
        относительных частот.
        Построить гистрограммы для полученных частот
        :param data: статистические данные
        :param interval_number: количество интервалов
        :return: интервальный ряд чатот и интервальный ряд
        относительных частот
        """
        # Построение таблицы
        interval_number = len(intervals)
        table = PrettyTable()
        table.add_column("Номер интервала - i", [i for i in range(1, interval_number + 1)])
        table.add_column("Частичный интервал", [f'{i[0]:0.3f}-{i[1]:0.3f}' for i in intervals])
        table.add_column("Сумма частот интервала", freq)
        table.add_column("Сумма относительных частот интервала", [f'{i:0.3f}' for i in rel_freq])

        # Построение гистрограммы
        # plt.hist(data, bins=interval_number, color='skyblue', edgecolor='black')
        # plt.title("Гистограмма")
        return table

    def solveC2(self, intervals: list[list[int]], freq: list[int], rel_freq: list[float]) -> PrettyTable:
        """
        Построить группированный ряд распределения частот
        и группированный ряд распрееделение относительных частот.
        Построить соответствующие полигоны.
        :param data: статистические данные
        :param interval_number: оличество интервалов
        :return: Групированный ряд распределения частот
        и относительных частот
        """
        middle = [(i[0] + i[1]) / 2 for i in intervals]
        # Получение группированного ряда распределения

        table = PrettyTable()
        table.add_column("Середина интервала", [f'{i:0.3f}' for i in middle])
        table.add_column("Частоты", freq)
        table.add_column("Относительных частоты", [f'{i:0.3f}' for i in rel_freq])

        # Построение полигонов
        fig1, pol1 = plt.subplots()
        fig1, pol2 = plt.subplots()

        pol1.plot(middle, freq)
        pol1.set_title("Полигон частот")

        pol2.plot(middle, rel_freq)
        pol2.set_title("Полигон относительных частот")

        return table

    def solveD2(self, intervals: list[list[int]], freq: list[int], rel_freq: list[float]) -> tuple[list[str], list[str]]:
        """
        Решить задачу D2:
        Дать определение функции распределения;
        Найти функции распределений
        для интервального и группированного рядов;
        Построить график для функциий.
        :param data: статистические данные
        :param interval_number: количество интервалов
        :return: функции распределения
        """

        P = rel_freq
        
        # получение эмпирической ф-ции распределения для интервального ряда
        p = 0
        Fx = [p := p + i for i in P]
        # получаем строковое представленние функции для интер. ряда
        str_intervals = ([f'x <= {intervals[0][0]:.3f}'] 
                         + [f'{i[0]} < x <= {i[1]:.3f}' for i in intervals] 
                         + [f'x > {intervals[-1][1]:.3f}'])
        Fx1 = [0] + Fx + [1]
        str_interv_Fx = [f'если {xs} то F*(x) = {p}' for p, xs in zip([f'{p:0.3f}' for p in Fx1], str_intervals)]


        # построение графика ф-ции для инт. ряда
        X_axis = [intervals[0][0]] + [i[1] for i in intervals]
        Y_axis = [0] + Fx
        fig1, intervals_graph = plt.subplots()
        intervals_graph.plot(X_axis, Y_axis)
        intervals_graph.set_title("График эмпирической функции для интервального ряда")

        # получение эмпирической ф-ции распределения для груп. ряда
            # получение груп. ряда
        mid = [(i[0] + i[1]) / 2 for i in intervals]
            # получение функции груп. ряда
        intervals = [(mid[0] - 1, mid[0])]
        for i in range(0, len(mid) - 1):
            intervals.append((mid[i], mid[i + 1]))
        intervals += [(mid[-1], mid[-1] + 1)]
             # получаем строковое представленние функции груп. ряда
        str_intervals = ([f'x <= {mid[0]:.3f}']
                         + [f'{i[0]:.3f} < x <= {i[1]:.3f}' for i in intervals[1:-1]]
                         + [f'x > {mid[-1]:.3f}'])
        str_grup_Fx = [f'если {xs} то F*(x) = {p}' for p, xs in zip([f'{p:0.3f}' for p in Fx1], str_intervals)]


        # построение графика ф-ции для груп.. ряда
        self.sublot_empirical_distribution_func(mid, P, "Эмпирическая функция распределения для группированного ряда")

        return str_interv_Fx , str_grup_Fx

    def solveE2(self, intervals: list[list[int]], freq: list[int]) -> tuple[str, float, str, float, str, float, str, float]:
        """
        Решить задачу E2:
        Дать определение функции распределения;
        Найти функции распределений
        для интервального и группированного рядов;
        Построить график для функциий.
        :param data: статистические данные
        :param interval_number: количество интервалов
        :return: функции распределения
        """

        X = [(i[0] + i[1]) / 2 for i in intervals]
        N = freq
        return (
            self._sample_mean,
            self.sample_mean(X, N),
            self._dispersion,
            self.dispersion(X, N),
            self._standard_deviation,
            self.standard_deviation(X, N),
            self._unbiased_assessment,
            self.unbiased_assessment(X, N)
        )


if __name__ == "__main__":
    data = [1, 1, 5, 3, 7, 1, 3]
    for a in Calculator().solveD2(data, 10):
        print("-" * 40)
        for s in a:
            print(s)
    # plt.show()