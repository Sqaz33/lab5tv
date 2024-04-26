
import seaborn as sns
# import matplotlib as plt
# import random

class Calculator:

    def solveB1(self, data: list[float]) -> list[float]:
        return list(sorted(set(data)))

    # def solveB2(seld, data: list[float], number_of_interval: int) -> tuple(list[float], list[float], list[float]):
    #     pass

    def solveC1(self, data: list[float]): #-> tuple(list[list[float]], list[list[float]], sns, sns):
        count = dict()
        for i in data:
            count[i] = count.get(i, 0) + 1

        freq = []
        for i in sorted(count.keys()):
            freq.append(count[i])

        relative_freq = [i / sum(freq) for i in freq]



    # def solveC2(self, data: list[float]) -> tuple(list[float], list[float], graph):
    # def solveD1:
    # def solveD2:
    # def solveE1::
    # def solveE2:


if __name__ == "__main__":
    # calc = Calculator()
    # print(calc.solveC1([1, 3, 1, 3, 3, 2, 2, 2, 5, 4, 4]))

    fmri = sns.load_dataset("fmri")
    sns.relplot(
        data=fmri, kind="line",
        x="timepoint", y="signal", col="region",
        hue="event", style="event",
    )
    sns.catplot(data=[1, 3, 1, 3, 3, 2, 2, 2, 5, 4, 4], kind="bar", x="day", y="total_bill", hue="smoker")
