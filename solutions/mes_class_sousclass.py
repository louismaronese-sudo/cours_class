#fichier ou je crée mes classes et mes sous classes

class Film :
    def __init__(self, name, year, director="Luc Besson" ):
        self.title = name
        self.year = year
        self.director = director

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}"

    def watch(self):
        print(f"Bon visionnage du film {self.title} ({self.year}), directed by {self.director}. Enjoy the movie!")

class FilmCassette(Film):
    pass
