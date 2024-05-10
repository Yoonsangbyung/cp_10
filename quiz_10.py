import random


def create_lotto_numbers():
    lotto_numbers = []


    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)
        if number not in lotto_numbers:
            lotto_numbers.append(number)

    lotto_numbers.sort()

    return "생성된 로또 번호는 {} 입니다".format(' '.join(map(str, lotto_numbers)))


print(create_lotto_numbers())

