from random import randint
from setup import *

class Dict:

    def __init__(self, level, sound):

        self.level = level
        self.sound = sound

        self.dict_lvl01 = [["CAT", "КОШКА"],
                     ["DOG", "СОБАКА"],
                     ["PEN", "РУЧКА"],
                     ["BED", "КРОВАТЬ"],
                     ["BAG", "СУМКА"]]

        self.dict_lvl02 = [["HOUSE", "ДОМ"],
                     ["WATER", "ВОДА"],
                     ["FLOWER", "ЦВЕТОК"],
                     ["GREEN", "ЗЕЛЁНЫЙ"],
                     ["DOOR", "ДВЕРЬ"]]

        self.dict_lvl03 = [["PENCIL", "КАРАНДАШ"],
                           ["SCHOOL", "ШКОЛА"],
                           ["WORLD", "МИР"],
                           ["DOOR", "ДВЕРЬ"],
                           ["CHAIR", "СТУЛ"]]

        self.dict_lvl04 = [["HOUSE", "ДОМ"],
                     ["CAT", "КОШКА"],
                     ["DOG", "СОБАКА"],
                     ["WATER", "ВОДА"],
                     ["FLOWER", "ЦВЕТОК"]]
        self.dict_lvl05 = [["GREEN", "ЗЕЛЁНЫЙ"],
                     ["PEN", "РУЧКА"],
                     ["PENCIL", "КАРАНДАШ"],
                     ["SCHOOL", "ШКОЛА"],
                     ["WORLD", "МИР"]]
        self.dict_lvl06 = [["DOOR", "ДВЕРЬ"],
                     ["CHAIR", "СТУЛ"],
                     ["BED", "КРОВАТЬ"],
                     ["APPLE", "ЯБЛОКО"],
                     ["TABLE", "СТОЛ"]]
        self.dict_lvl07 = [["BLACK", "ЧЁРНЫЙ"],
                     ["MOTHER", "МАМА"],
                     ["FATHER", "ПАПА"],
                     ["BAG", "СУМКА"],
                     ["HAND", "РУКА"]]
        self.dict_lvl08 = [['', ''],
                           ['', ''],
                           ['', ''],
                           ['', ''],
                           ['', '']]
        self.dict_lvl09 = [['ELABORATE', 'РАЗРАБАТЫВАТЬ'],
                           ['HUMILATE', 'УНИЖАТЬ'],
                           ['UNIFY', 'ОБЪЕДИНЯТЬ'],
                           ['EVADE', 'ОБОЙТИ'],
                           ['SURRENDER', 'СДАВАТЬСЯ']]
        self.dict_lvl10 = [['COLLAPSE', 'РАЗРУШАТЬСЯ'],
                            ['CONVENIENT', 'УДОБНЫЙ' ],
                            ['DEPTH', 'ГЛУБИНА'],
                            ['DETERIORATE', 'УХУДШАТЬ'],
                            ['DISTRICT', 'РАЙОН'],
                            ['ENTOURAGE', 'ОКРУЖЕНИЕ']]


        self.dict = []
        self.dict.append(self.dict_lvl01)
        self.dict.append(self.dict_lvl02)
        self.dict.append(self.dict_lvl03)
        self.dict.append(self.dict_lvl04)

        # self.current_word = randint(0, len(self.dict[level]) - 1)
        self.current_word = 0

        self.marker_chars = self.get_marker_chars()
        print(self.marker_chars)

    def get_word(self, number):
        if (self.current_word < len(self.dict[self.level])):
            return self.dict[self.level][self.current_word][number]
        return " " * 30

    def is_word_complete(self):
        res = True
        for i in range(len(self.marker_chars)):
            res = res and self.marker_chars[i]
        return res

    def get_marker_chars(self):
        ret = []
        for i in range(len(self.dict[self.level][self.current_word][0])):
            ret.append(False)
        return ret

    def inc_number_word(self):
        self.current_word += 1
        if (self.current_word ==  len(self.dict[self.level])):
            return False
        self.sound.play(self.sound.SHOOT)
        self.marker_chars = self.get_marker_chars()
        return True

