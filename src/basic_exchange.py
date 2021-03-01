

class Basic_Exchange:
    def __init__(self, weight, height, age, gender, correction_coefficient):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.correction_coefficient = correction_coefficient

    def formula_base_exchange(self, weight, height, age, gender, correction_coefficient):
        base_exchange = (10 * weight) + (6.25 * height) - (5 * age) + correction_coefficient
        return base_exchange


