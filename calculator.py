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

    # -------------решения задач-------------------------
    def solveB1(self, data: list[float]) -> list[float]:
        """
        Решить задачу B1:
        составить вариационный ряд
        :param data: статистические данные
        :return: вариацонный ряд
        """
        return list(sorted(set(data)))

    def solveB2(self, data: list[float], intervals_number: int):
        raise "234"

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

    def solveC2(self, data: list[float]) -> tuple[list[float], list[float]]:
        pass

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
            plt.plot([intervals[i][1], intervals[i][1]], [Fx[i], Fx[i + 1]], linestyle="--", color="black")

        # получаем строковое представленние функции
        str_intervals = ([f'x <= {X[0]}']
                         + [f'{i[0]} < x <= {i[1]}' for i in intervals[1:len(intervals) - 1]]
                         + [f'x > {X[-1]}'])
        str_Fx = [f'если {xs} то F*(x) = {p}' for p, xs in zip([f'{p:0.3f}' for p in Fx], str_intervals)]

        return func_definition, str_Fx

    def solveD2(self):
        pass

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

    def solveE2(self):
        pass


if __name__ == "__main__":
    # calc = Calculator()
    # data = []

    # # Отображение графика
    # ans = calc.solveD1(data)
    # print(ans[0])
    # for s in ans[1]:
    #     print(s)
    # plt.show()
    Calculator().solveB2([], 123)
