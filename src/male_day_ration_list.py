from basic_exchange import Basic_Exchange

correction_coefficient = 5
weight = 57
height = 173
age = 38
gender = 'M'


class Male_Day_Ration_List(Basic_Exchange):
    def male_day_ration_list(self):
        formula_base_exchange = Basic_Exchange(weight, height, age, gender, correction_coefficient)
        print(formula_base_exchange.correction_coefficient)
        male_base_exchange = formula_base_exchange.formula_base_exchange(weight, height, age, gender, correction_coefficient)
        print(male_base_exchange)


    if __name__ == "__main__":
        female_day_ration_list(self=male_day_ration_list)
