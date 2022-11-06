class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)

    @classmethod
    def add_to_genres(cls, genre):
        cls.add_to_genre_count(genre)
        if not genre in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        cls.add_to_artist_count(artist)
        if not artist in cls.artists:
            cls.artists.append(artist)

    @classmethod 
    def add_to_genre_count(self, genre):
        try:
            self.genre_count[genre] += 1
        except:
            self.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(self, artist):
        try:
            self.artist_count[artist] += 1
        except:
            self.artist_count[artist] = 1