from spoopify.song import Song
from spoopify.album import Album


class Band:
    name: str
    albums: list

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        album = album
        name_of_album = album.name
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {name_of_album}."
        else:
            return f"Band {self.name} already has {name_of_album} in their library."

    def remove_album(self, album_name: str):
        all_album_names = [a.name for a in self.albums]
        if album_name in all_album_names:
            for a in self.albums:
                if a.name == album_name and a.published == True:
                    return f"Album has been published. It cannot be removed."
                elif a.name == album_name and a.published == False:
                    self.albums.remove(a)
                    return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        res = f"Band {self.name}"
        for a in self.albums:
            res += f"\n{a.details()}"
        return res

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

