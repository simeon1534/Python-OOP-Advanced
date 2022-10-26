class ExercisePlan:
    exercise_plan_id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration  # MINUTES
        ExercisePlan.exercise_plan_id += 1
        self.exercise_plan_instance_id = ExercisePlan.exercise_plan_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):  # FACTORY
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.exercise_plan_id + 1

    def __repr__(self):
        return f"Plan <{ExercisePlan.exercise_plan_id}> with duration {self.duration} minutes"


