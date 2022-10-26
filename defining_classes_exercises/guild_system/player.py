class Player:
    name: str
    hp: int
    mp: int

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        skills_res = "\n".join([f"==={skill} - {self.skills[skill]}" for skill in self.skills])
        res = [f"Name: {self.name}",
               f"Guild: {self.guild}",
               f"HP: {self.hp}",
               f"MP: {self.mp}",
               skills_res]
        return "\n".join(res)


