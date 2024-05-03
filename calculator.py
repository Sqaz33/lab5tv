import matplotlib.pyplot as plt
from prettytable import PrettyTable


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
        S = n/(n - 1) * D_в        
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
        return n / (n - 1) * self.dispersion(variation_series, frequencies)

    def get_intervals(self, data: list[float], interval_number: int) -> list[list[int]]:
        var = self.solveB1(data)
        mx = max(var)
        mn = min(var)
        step = (mx - mn) / interval_number
        intervals = []
        x = mn
        while x + step <= mx:
            intervals.append([x, x := x + step])
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
        for i in range(len(var)):
            if var[i] == intervals[-1][1]:
                rel_freq[-1] += var_rel_freq[i]
        return rel_freq
    
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

        # получение интервалов, для значения ф-ции распр.
        intervals = [(X[0] - 1, X[0])]
        for i in range(0, len(X) - 1):
            intervals.append((X[i], X[i + 1]))
        intervals += [(X[-1], X[-1] + 1)]

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
            # добавление пунктира
        for i in range(len(Fx) - 1):
            plt.plot(
                [intervals[i][1], intervals[i][1]], [Fx[i], Fx[i + 1]], linestyle="--", color="black"
                )

        # получаем строковое представленние функции
        str_intervals = ([f'x <= {X[0]}']
                         + [f'{i[0]} < x <= {i[1]}' for i in intervals[1:len(intervals) - 1]]
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
    def solveB2(self, data: list[float], interval_number: int) -> PrettyTable:
        assert interval_number > 0, "Невозмножно построить интервалы"

        var = self.solveB1(data)

        # Получение интервалов
        intervals = self.get_intervals(data, interval_number)

        # Получение интервального ряда частот и относ. частот
        freq = self.get_intervals_frequencies(data, interval_number)
        rel_freq = self.get_intervals_relative_frequencies(data, interval_number)

        # Построение таблицы
        table = PrettyTable()
        table.add_column("Номер интервала - i", [i for i in range(1, interval_number + 1)])
        table.add_column("Частичный интервал", [f'{i[0]:0.3f}-{i[1]:0.3f}' for i in intervals])
        table.add_column("Сумма частот интервала", freq)
        table.add_column("Сумма относительных частот интервала", [f'{i:0.3f}' for i in rel_freq])

        # Построение гистрограмм
        plt.hist(data, bins=interval_number, color='skyblue', edgecolor='black')
        plt.title("Гистограмма")
        return table

    def solveC2(self, data: list[float], interval_number: int) -> PrettyTable:
        middle = [(i[0] + i[1]) / 2 for i in self.get_intervals(data, interval_number)]
        # Получение группированного ряда распределения
        freq = self.get_intervals_frequencies(data, interval_number)
        relative_freq = self.get_intervals_relative_frequencies(data, interval_number)

        table = PrettyTable()
        table.add_column("Середина интервала", [f'{i:0.3f}' for i in middle])
        table.add_column("Частоты", freq)
        table.add_column("Относительных частоты", [f'{i:0.3f}' for i in relative_freq])

        # Построение полигонов
        fig1, pol1 = plt.subplots()
        fig1, pol2 = plt.subplots()

        pol1.plot(middle, freq)
        pol1.set_title("Полигон частот")

        pol2.plot(middle, relative_freq)
        pol2.set_title("Полигон относительных частот")

        return table

    def solveD2(self):
        pass

    def solveE2(self):
        pass


if __name__ == "__main__":

    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

    print(Calculator().solveC2(data, 10))
    plt.show()