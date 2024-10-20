from threading import Thread

def calculate(power_degree):
    for i in range(1, 11):
        print(f"Число {i} в степени {power_degree}: {i**power_degree}")

if __name__ == '__main__':
    thread_square = Thread(target=calculate, args=(2,))
    # Передаем 2 как аргумент
    thread_cube = Thread(target=calculate, args=(3,))
    # Передаем 3 как аргумент

    thread_square.start()
    thread_cube.start()

    thread_square.join()
    thread_cube.join()
