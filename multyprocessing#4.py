import multiprocessing
import os
import math

"""
Задание 4.
Напишите программу, которая использует многопроцессность 
для вычисления факториала целых чисел от 1 до 10. 
Каждый процесс должен вычислять факториал одного числа.
"""

def calculate_factorial(number):
    """Вычисляет факториал числа."""
    print(f"Процесс {os.getpid()}: вычисление факториала {number}")
    result = math.factorial(number)
    print(f"Процесс {os.getpid()}: факториал {number} = {result}")
    return result

if __name__ == "__main__":
    numbers = list(range(1, 11))  # Числа от 1 до 10
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=calculate_factorial, args=(number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Все процессы завершены.")