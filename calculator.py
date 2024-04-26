import matplotlib.pyplot as plt
from prettytable import PrettyTable


class Calculator:

    def solveB1(self, data: list[float]) -> list[float]:
        return list(sorted(set(data)))

    # def solveB2(seld, data: list[float], number_of_interval: int) -> tuple(list[float], list[float], list[float]):
    #     pass

    def solveC1(self, data: list[float]) -> tuple[PrettyTable, PrettyTable]:
        count = dict()
        for i in data:
            count[i] = count.get(i, 0) + 1

        freq = []
        for i in sorted(count.keys()):
            freq.append(count[i])

        relative_freq = [i / sum(freq) for i in freq]

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
    def solveD1(self):
        pass
    # def solveD2:
    # def solveE1::
    # def solveE2:


if __name__ == "__main__":
    # calc = Calculator()
    # for t in calc.solveC1([1, 3, 1, 3, 3, 2, 2, 2, 5, 4, 4, 4, 4, 4, 4, 4]):
    #     print(t)
    x = [1, 4, 4, 6, 6, 16]
    y = [0.2, 0.2, 0.5, 0.5, 1, 1]
    plt.plot(x, y)
    plt.show()