class Song:
    count = 0
    genre = []
    artists = []
    genre_count = []
    artists_count = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
