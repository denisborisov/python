'''
Task 1.

Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

print("\n***** Task 1 *****")
print("\n>Let's play with a class.")

import time

class TrafficLight:
    __color = 'RED'

    def running(self):
        self.light('RED', 7)
        self.light('YELLOW', 2)
        self.light('GREEN', 5)

    def light(self, color, color_time):
        self.__color = color
        print(self.__color, end=':\t')
        t1 = time.time()
        seconds = 1
        while time.time() - t1 <= color_time:
            if time.time() - t1 >= seconds:
                print(seconds, end=' ')
                seconds += 1
        print()

traffic_light = TrafficLight()
traffic_light.running()