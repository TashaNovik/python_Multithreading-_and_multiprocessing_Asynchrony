from threading import Thread
from time import sleep

"""
Задание 2. Напишите программу, которая создаёт несколько потоков
для выполнения функции,
которая выводит целые числа от 1 до 10 с задержкой в 1 секунду.
"""

def print_numbers_from_1_to_10(thread_num):
    for i in range(1,11):
        print(f"Thread {thread_num}: {i}")
        sleep(1)

if __name__ == '__main__':
    threads_list = []
    for i in range(5):
        current_thread = Thread(target=print_numbers_from_1_to_10,args=(i,))
        threads_list.append(current_thread)
        current_thread.start()

        for current_thread in threads_list:
            current_thread.join()
