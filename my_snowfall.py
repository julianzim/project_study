# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

tick = 0
snowflakes = {}
sd.resolution = (1200, 750)

class Snowflake:
    size = {'min': 10, 'max': 20}

    def __init__(self):
        self.x = random.randint(0, sd.resolution[0])
        self.y = random.randint(sd.resolution[1] - 100,
                                sd.resolution[1] + 100)
        self.length = random.randint(10, 20)

    def clear_previous_picture(self, color=sd.background_color):
        self.draw(color)

    def move(self):
        self.x += random.randint(-5, 5)
        # self.y -= 5
        self.y -= Snowflake.size['max'] + 1 - self.length

    def draw(self, color=sd.COLOR_WHITE):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(point, self.length, color)

def snowfall(snowflakes_count):
    if len(snowflakes) != snowflakes_count:
        snowflakes[len(snowflakes)] = Snowflake()
    for num, snowflake in snowflakes.items():
        snowflake.clear_previous_picture()
        snowflake.move()
        snowflake.draw()
        if snowflake.y < random.randint(-2, 2):
            snowflakes[num] = Snowflake()

while True:
    tick += 1
    sd.start_drawing()

    if tick < 50:
        snowfall(20)
    elif tick > 50:
        snowfall(50)

    sd.sleep(0.05)
    sd.finish_drawing()

    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
