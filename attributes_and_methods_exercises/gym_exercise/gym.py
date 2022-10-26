from gym_exercise.customer import Customer
from gym_exercise.trainer import Trainer
from gym_exercise.equipment import Equipment
from gym_exercise.subscription import Subscription
from gym_exercise.exercise_plan import ExercisePlan


class Gym:
    def __init__(self):
        self.customers = []  # CUSTOMER OBJ
        self.trainers = []  # TRAINER OBJ
        self.equipment = []  # EQUIPMENT OBJ
        self.plans = []  # PLAN OBJ
        self.subscriptions = []  # SUBSCRIPTION OBJ

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        # subscription, the customer and trainer to it, the plan to that trainer and the equipment
        res = []
        for subsc in self.subscriptions:
            if subsc.sub_id == subscription_id:
                res.append(subsc.__repr__())
                for customer in self.customers:
                    if customer.customer_instance_id == subsc.customer_id:
                        res.append(customer.__repr__())
                        for trainer in self.trainers:
                            if trainer.trainer_instance_id == subsc.trainer_id:
                                res.append(trainer.__repr__())
                                for exercise_plan in self.plans:
                                    if exercise_plan.exercise_plan_instance_id ==subsc.exercise_id:
                                        for equipment in self.equipment:
                                            if equipment.equipment_instance_id == exercise_plan.equipment_id:
                                                res.append(equipment.__repr__())
                                                res.append(exercise_plan.__repr__())

        return '\n'.join(res)

