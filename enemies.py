# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    answer = None
    quest = None
    pass


def generate_random_enemy(num):
    random_enemy_type = choice(enemy_types)
    enemy = random_enemy_type()
    print('Дракон {} создан'.format(num))
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy(i) for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.answer = answer
        print(answer)

    def check_answer(self, answer):
        return answer == self.answer


class GreenDragon(Dragon):
    def __init__(self):
        self.health = 200
        self.attack = 10
        self.color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.quest


class RedDragon(Dragon):
    def __init__(self):
        self.health = 200
        self.attack = 10
        self.color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.quest


class BlackDragon(Dragon):
    def __init__(self):
        self.health = 200
        self.attack_strength = 10
        self.color = 'черный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.quest


enemy_types = [GreenDragon, RedDragon, BlackDragon]
