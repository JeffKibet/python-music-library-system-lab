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

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list, keeping entries unique."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list, keeping entries unique."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the count for this genre, creating the key
        with a starting value of 1 if it doesn't exist yet."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the count for this artist, creating the key
        with a starting value of 1 if it doesn't exist yet."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1