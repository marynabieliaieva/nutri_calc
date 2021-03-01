from basic_exchange import Basic_Exchange
from physical_activity_factor import Physical_Activity_Factor

correction_coefficient = (-161)
weight = 57
height = 173
age = 38
gender = 'F'
steps = 4500
workout = 1


class Female_Day_Ration_List(Basic_Exchange, Physical_Activity_Factor):
    def female_day_ration_list(self):
        formula_base_exchange = Basic_Exchange(weight, height, age, gender, correction_coefficient)
        print(formula_base_exchange.correction_coefficient)
        female_base_exchange = formula_base_exchange.formula_base_exchange(weight, height, age, gender, correction_coefficient)
        print(female_base_exchange)

        physical_activity_factor_count = Physical_Activity_Factor(steps, workout)
        print(physical_activity_factor_count.steps)
        female_physical_activity_factor = physical_activity_factor_count.physical_activity_factor_count(steps, workout)
        print(female_physical_activity_factor)

        daily_energy_consumption = female_base_exchange * female_physical_activity_factor
        print(daily_energy_consumption)

    if __name__ == "__main__":
        female_day_ration_list(self=female_day_ration_list)
