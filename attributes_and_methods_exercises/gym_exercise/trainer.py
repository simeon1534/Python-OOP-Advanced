class Trainer:
    trainer_id = 0

    def __init__(self, name: str):
        self.name = name
        Trainer.trainer_id += 1
        self.trainer_instance_id = Trainer.trainer_id
    def __repr__(self):
        return f"Trainer <{Trainer.trainer_id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.trainer_id + 1