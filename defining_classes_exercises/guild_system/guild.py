from guild_system.player import Player


class Guild:
    name: str
    list_of_players: list

    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        players_names = [p.name for p in self.list_of_players]
        if player_name in players_names:
            for p in self.list_of_players:
                if p.name == player_name:
                    p.guild = "Unaffiliated"
                    self.list_of_players.remove(p)
                    return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        names = ''
        for player_object in self.list_of_players:
            names += f"{player_object.player_info()}\n"
        res = [f"Guild: {self.name}\n", names]

        return ''.join(res)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
