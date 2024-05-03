import random


class Generator:
    """
        3. Составить файл из статистических данных, содержащий от 50 до 80
        целых чисел, среди которых количество различных вариантов должно
        быть не менее 10 и не более 20 (числа могут быть как одного, так и разных
        знаков).
    """

    @staticmethod
    def generate_list_of_number(
            amount_of_numbers: int,
            values: tuple[int, int],
            freq: tuple[int, int]
    ) -> list[...]:
        # составить вар. ряд с частотами
        # оч медленное решение при малом количестве вариантов------------------
        rands = dict()
        sum_freq = 0
        while sum_freq < amount_of_numbers:
            rand_val = random.randint(values[0], values[1])
            rand_freq = random.randint(freq[0], freq[1])
            if rands.get(rand_val, "not") == "not":
                rands[rand_val] = rand_freq
                sum_freq += rand_freq
        #------------------------------------------

        # подбить сумму частот до треб. кол. чисел
        while sum_freq != amount_of_numbers:
            for n in rands.keys():
                if sum_freq == amount_of_numbers:
                    break
                if rands[n] >= freq[0] + 1:
                    rands[n] -= 1
                    sum_freq -= 1

        # составить список случайных чисел
        stats = []
        for n in rands.keys():
            stats += [n] * rands[n]
        random.shuffle(stats)

        return stats


if __name__ == "__main__":
    Generator.generate_list_of_number(100, (-10, 10), (10, 20))
