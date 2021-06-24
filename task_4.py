import random

def func():
    def wrapper(times):
        for i in range(times):
            number = random.randrange(1, 101)
            print(f"Ваше случайное число - {number}")
        print(f'Функция отработала {i + 1} раз')
    return wrapper(7)
func()
