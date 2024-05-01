import matplotlib.pyplot as plt
from prettytable import PrettyTable

class Calculator:

    def get_frequencies(self, data: list[float]) -> list[int]:
        count = dict()
        for i in data:
            count[i] = count.get(i, 0) + 1
        freq = []
        for i in sorted(count.keys()):
            freq.append(count[i])
        return freq

    def get_relative_frequencies(self, data: list[float]) -> list[float]:
        freq = self.get_frequencies(data)
        return [i / sum(freq) for i in freq]

    def solveB1(self, data: list[float]) -> list[float]:

        return list(sorted(set(data)))

    def solveC1(self, data: list[float]) -> tuple[PrettyTable, PrettyTable]:

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
        func_definition = ("Эмпирической функцией распредления называют функцию F*(x), определяющую для каждого значения x "
                           "относительну частоту события X < x: F*(x) = n_x/n")

        X = self.solveB1(data)
        P = self.get_relative_frequencies(data)
        p = 0
        Fx = [0] + [p := p + i for i in P]
        Fx = [f'{p:0.2f}' for p in Fx]

        intervals = [f'x < {X[0]}']
        for i in range(0, len(X) - 1):
            intervals.append(f'{X[i]} < x <= {X[i + 1]}')
        intervals += [f'x > {X[-1]}']

        ans = [f'если {xs} то F*(x) = {p}' for p, xs in zip(Fx, intervals)]

        return func_definition, ans

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


