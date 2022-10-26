from hard.hardware import Hardware
from hard.power_hardware import PowerHardware
from hard.heavy_hardware import HeavyHardware
from soft.express_software import ExpressSoftware
from soft.light_software import LightSoftware


class System:
    _software = []  # software objects
    _hardware = []  # hardware objects

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, 'Power', capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, 'Heavy', capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        there_is_hardware_obj = False

        for hardware_obj in System._hardware:
            if hardware_obj.name == hardware_name:
                there_is_hardware_obj = True
                express_software = ExpressSoftware(name, 'Express', capacity_consumption, memory_consumption)
                hardware_obj.install(express_software)
                System._software.append(express_software)

        if not there_is_hardware_obj:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        there_is_hardware_obj = False
        for hardware_obj in System._hardware:
            if hardware_obj.name == hardware_name:
                there_is_hardware_obj = True
                light_software = LightSoftware(name, 'Light', capacity_consumption, memory_consumption)
                hardware_obj.install(light_software)
                System._software.append(light_software)
        if not there_is_hardware_obj:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        there_is_hardware_name = False
        there_is_software_name = False
        h_object = None
        s_object = None

        for hardware_obj in System._hardware:
            if hardware_obj.name == hardware_name:
                there_is_hardware_name = True
                h_object = hardware_obj

        for software_obj in System._software:
            if software_obj.name == software_name:
                there_is_software_name = True
                s_object = software_obj

        if there_is_hardware_name and there_is_software_name:
            h_object.uninstall(s_object)
            System._software.remove(s_object)

        else:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():

        hardware_components = len(System._hardware)
        software_components = len(System._software)

        total_memory_consuption = sum([s_obj.memory_consumption for s_obj in System._software])
        total_memory = sum([h_obj.memory for h_obj in System._hardware])

        total_capacity_consuption = sum([s_obj.capacity_consumption for s_obj in System._software])
        total_capacity = sum([h_obj.capacity for h_obj in System._hardware])

        return f'System Analysis \n Hardware Components: {hardware_components} \n Software Components: {software_components} \n /' \
               f'Total Operational Memory: {total_memory_consuption} \\ {total_memory} \n Total Capacity Taken: {total_capacity_consuption} \\ {total_capacity}'

    @staticmethod
    def system_split():
        stats = []
        for hardware_obj in System._hardware:
            stats.append(f"Hardware Component - {hardware_obj.name}\n")
            express = 0
            light = 0
            memory_total_software = 0
            capacity_total_software = 0
            software_components = []
            for software in hardware_obj.software_components:
                if isinstance(software,LightSoftware):
                    light+=1
                if isinstance(software,ExpressSoftware):
                    express+=1
                memory_total_software += software.memory_consumption
                capacity_total_software += software.capacity_consumption
                software_components.append(software.name)

            stats.append(f"Express Software Components: {express}\n")
            stats.append(f"Light Software Components: {light}\n")
            stats.append(f"Memory Usage: {memory_total_software} / {hardware_obj.memory}\n")
            stats.append(f"Capacity Usage: {capacity_total_software} / {hardware_obj.capacity}\n")
            stats.append(f'Type: {hardware_obj.hardware_type}\n')
            if software_components:
                stats.append(f"Software Components: {', '.join(software_components)}\n")
            else:
                stats.append(f"Software Components: None\n")
        return ''.join(stats)
System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())

