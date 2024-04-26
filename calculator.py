
# import seaborn as sns
# import pandas as pd
# import numpy as np
# import matplotlib as plt
# import random

class Calculator:

    def solveB1(self, data: list[int]) -> list[int]:
        return list(sorted(set(data)))

    # def solveB2(seld, data: list[float], number_of_interval: int) -> tuple(list[float], list[float], graph):
    #     pass
    #
    # def solveC1(self, data: list[float]) -> tuple(list[float], list[float], graph):
    #     pass
    #
    # def solveC2(self, data: list[float]) -> tuple(list[float], list[float], graph):
    # def solveD1:
    # def solveD2:
    # def solveE1::
    # def solveE2:


if __name__ == "__main__":
    calc = Calculator()
    print(calc.solveB1([1, 1, 3, 3, 3, 2, 2, 2, 5, 4, 4]))