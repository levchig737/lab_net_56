import math
import datetime
import matplotlib.pyplot as plt


"""
Функция получения случайных a и b и с
"""


def get_random_a_b_c():
    now = datetime.datetime.now()
    seed = now.minute * 60

    c = math.ceil(seed)
    a = seed * 4 + 1
    b = seed * 8 + 3

    return a, b, c


"""
Функция ГПСЧ
Возвращает список или одно число
"""


def lin_rand_arr_flxd(size):
    a, b, seed = get_random_a_b_c()
    n = 24
    m = 2**n

    # Вывод значений
    print(
        f"""
    a = {a}
    b = {b}
    c = {seed}
    """
    )

    if size == 1:
        return [math.ceil(math.fmod(a * seed + b, m)) % 255]
    r = [0 for i in range(size + 1)]
    r[0] = math.ceil(seed)
    for i in range(1, size + 1):
        r[i] = math.ceil(math.fmod((a * r[i - 1] + b), m)) % 255

    return r[1 : size + 1]


"""
Функция вывода гистограммы
"""


def print_histogram(data):
    plt.hist(data, bins=100)
    plt.xlabel("Интервалы")
    plt.ylabel("Кол-во чисел")
    plt.show()


def main():
    while True:
        number = int(
            input(
                """Введите 
    1 - Сгенирировать последовательность 
    2 - Записать данные в файл
    3 - Вывести гистограмму 
    4 - если хотите выйти: """
            )
        )

        if number == 1:
            n = int(input("Введите размер последовательности: "))
            data = lin_rand_arr_flxd(n)

        if number == 2:
            f = open("output.txt", "w")

            for item in data:
                f.write("%s " % str(item))
            f.close()

        if number == 3:
            print_histogram(data)

        if number == 4:
            exit(0)


if __name__ == "__main__":
    main()
