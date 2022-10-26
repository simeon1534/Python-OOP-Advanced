

from soft.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.software_type = 'Light'
        self.capacity_consumption = int(capacity_consumption + (0.5 * capacity_consumption))
        self.memory_consumption = int(memory_consumption - (0.5 * memory_consumption))

