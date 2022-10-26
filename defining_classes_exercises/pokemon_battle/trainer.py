from pokemon_battle.pokemon import Pokemon
from typing import List


class Trainer:
    name: str
    pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemon:
            if pokemon.name ==pokemon_name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        res_trainer = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}"
        res_pok = [f"\n- {single_pokemon.pokemon_details()}" for single_pokemon in self.pokemon]
        # for single_pokemon in self.pokemon:
        #     single_pokemon: Pokemon
        #     res += f"\n - {single_pokemon.pokemon_details()}"
        return res_trainer+"\n".join(res_pok)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
