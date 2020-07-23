seconds = int(input("Введите количеко секунд, которые нужны перевести в нужный формат: "))

import time


def convert(seconds) :
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


print(convert(seconds))
