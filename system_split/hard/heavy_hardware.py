from hard.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        super().__init__(name, hardware_type, capacity, memory)
        self.hardware_type = 'Heavy'
        self.capacity = capacity * 2
        self.memory = int(0.75 * memory)
