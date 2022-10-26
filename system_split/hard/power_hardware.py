from hard.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        super().__init__(name, hardware_type, capacity, memory)
        self.hardware_type = 'Power'
        self.capacity = int(0.25 * capacity)
        self.memory = int(memory + (0.75 * memory))


