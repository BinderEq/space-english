from random import randint

class Dict:

    def __init__(self):
        self.current_word = 0
        self.dict = [["HOUSE", "ДОМ"],
                     ["CAT", "КОШКА"],
                     ["DOG", "СОБАКА"],
                     ["WATER", "ВОДА"],
                     ["FLOWER", "ЦВЕТОК"],
                     ["GREEN", "ЗЕЛЁНЫЙ"],
                     ["PEN", "РУЧКА"],
                     ["PENCIL", "КАРАНДАШ"],
                     ["SCHOOL", "ШКОЛА"],
                     ["WORLD", "МИР"],
                     ["DOOR", "ДВЕРЬ"],
                     ["CHAIR", "СТУЛ"],
                     ["BED", "КРОВАТЬ"],
                     ["APPLE", "ЯБЛОКО"],
                     ["TABLE", "СТОЛ"],
                     ["BLACK", "ЧЁРНЫЙ"],
                     ["MOTHER", "МАМА"],
                     ["FATHER", "ПАПА"],
                     ["BAG", "СУМКА"],
                     ["HAD", "РУКА"]]

        self.marker_chars = self.get_marker_chars()

    def get_marker_chars(self):
        ret = []
        for i in range(len(self.dict[self.current_word][0])):
            ret.append(False)
        return ret