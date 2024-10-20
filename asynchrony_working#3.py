import asyncio

"""
Задание 3.
Напишите программу, 
которая асинхронно обрабатывает список чисел, 
вычисляя их квадрат. 
Каждая операция обработки должна имитировать задержку в 1 секунду.
"""

async def calculate_square(number): # Изменено: функция теперь принимает одно число
    power_degree = 2
    await asyncio.sleep(1) # Использование asyncio.sleep()
    print(f"Число {number} в степени {power_degree}: {number**power_degree}")

async def main():
    number_list = [1, 4, 5, 6, 8, 81]
    tasks = [calculate_square(number) for number in number_list] # Создаем список задач
    await asyncio.gather(*tasks) # Запускаем задачи конкурентно

if __name__ == '__main__':
    asyncio.run(main())