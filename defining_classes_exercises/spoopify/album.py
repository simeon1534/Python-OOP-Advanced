from spoopify.song import Song


class Album:
    name: str
    list_of_songs: list
    published: bool

    def __init__(self, name: str, *args):
        self.name = name
        self.list_of_songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.list_of_songs:
            return f"Song is already in the album."
        elif self.published:
            return f"Cannot add songs. Album is published."
        else:
            self.list_of_songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        all_song_names = [s.name for s in self.list_of_songs]
        if song_name in all_song_names:
            if self.published:
                return "Cannot remove songs. Album is published."
            else:
                for s in self.list_of_songs:
                    if s.name == song_name:
                        return f"Removed song {song_name} from album {self.name}"
        else:
            return f"Song is not in the album."

    def publish(self):
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        res = f"Album {self.name}"
        for s in self.list_of_songs:
            res += f"\n== {s.get_info()}"
        return res


