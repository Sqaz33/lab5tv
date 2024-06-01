import random

class Generator:

    @staticmethod
    def generate_list_of_number(
            amount_of_numbers: int,
            values: tuple[int, int],
            freq: tuple[int, int],
    ) -> list[...]:
        # получить список чисел длинной amount_of_numbers 
        # частота каждого числа от freq[0] до freq[1] включительно
        # числа содержаться в диапазоне от values[0] до values[1] включительно
        assert freq[0] * (values[1] - values[0] + 1) >= amount_of_numbers, "Sum of freqs less, then amount_of_number"
        rnd = dict()
        while amount_of_numbers > 0:
            r = random.randint(values[0], values[1])
            if r not in rnd.keys():
                fr = random.randint(freq[0], freq[1]);
                if (freq[1] > amount_of_numbers):
                    fr = amount_of_numbers
                amount_of_numbers -= fr
                rnd[r] = fr
        
        series = []
        for k in rnd.keys():
            series += [k] * rnd[k]
        random.shuffle(series)
        
        return series 




if __name__ == "__main__":
    res = Generator.generate_list_of_number(1000, (-100, 100), (10, 20))
    for n in res:
        if res.count(n) < 10:
            print("huinya")
    print(len(res))
