class Equipment:
    equipment_id = 0

    def __init__(self, name: str):
        self.name = name
        Equipment.equipment_id += 1
        self.equipment_instance_id = Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{Equipment.equipment_id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id + 1

