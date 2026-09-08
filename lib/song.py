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

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    def __repr__(self):
        return f"<Song: '{self.name}' by {self.artist} ({self.genre})>"

    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1