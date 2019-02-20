from enum import Enum, auto


class MusicGenre(Enum):
    Rock = auto()
    Country = auto()
    Pop = auto()
    Classical = auto()
    Rap = auto()
    Blues = auto()


# equivelant:
MusicGenre = Enum('MusicGenre', 'Rock Country Pop Classical Rap Blues')


class Song:
    def __init__(self, name: str, artist: str, year: int, genre: MusicGenre):
        self.name = name
        self.artist = artist
        self.year = year
        self.genre = genre

    @property
    def will_dee_snider_like_it(self):
        return self.genre == MusicGenre.Rock
