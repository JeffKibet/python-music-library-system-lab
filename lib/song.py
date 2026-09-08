class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    def __repr__(self):
        return f"<Song: '{self.name}' by {self.artist} ({self.genre})>"

    @classmethod
    def add_song_to_count(cls):
        
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

if __name__ == "__main__":
    song1 = Song("Alright", "Kendrick Lamar", "Rap")
    song2 = Song("HUMBLE.", "Kendrick Lamar", "Rap")
    song3 = Song("Blinding Lights", "The Weeknd", "Pop")
    song4 = Song("Old Town Road", "Lil Nas X", "Country")
 
    print("Total songs:", Song.count)
    print("All artists:", Song.artists)
    print("All genres:", Song.genres)
    print("Genre counts:", Song.genre_count)
    print("Artist counts:", Song.artists_count)