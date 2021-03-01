class Physical_Activity_Factor:
    def __init__(self, steps, workout):
        self.steps = steps
        self.workout = workout

    def physical_activity_factor_count(self, steps, workout):
        if steps < 5000 and workout < 2:
            physical_activity_factor = 1.2
        elif steps > 5001 and steps < 10000 and workout > 2 and workout < 3:
            physical_activity_factor = 1.3
        elif steps > 10001 and workout > 4:
            physical_activity_factor = 1.4
        return physical_activity_factor
