#fichier ou je crée mes classes et mes sous classes

class Film :
    def __init__(self, name, year, director="Luc Besson" ):
        self.title = name
        self.year = year
        self.director = director

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}"

    def watch(self, player):
        print(f"Bon visionnage du film {self.title} ({self.year}), directed by {self.director}. Enjoy the film badass!")

class FilmCassette(Film):
    def __init__(self, name, year, director="Luc Besson"):
        self.title = name
        self.year = year
        self.director = director        
        self.format = "VHR"
        self.magnetic_tape = True

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director} on VHR"

    def rewind(self):
        print(f"Rewind the magnetic tape of {self.title} ({self.year}), directed by {self.director}.")
        self.magnetic_tape = False

    def watch(self, player):
        # Regarde le film 
        if player.type != "VHR":
            print(f"Cannot watch {self.title} ({self.year}), directed by {self.director} on a {player.type} player. Please use a VHR player.")
        else:
            print(f"Bon visionnage du film {self.title} ({self.year}), directed by {self.director} on a VHR player. Enjoy the movie!")
            super().watch(player)  # Appelle la méthode watch de la classe Film

class Player:
    # un lecteur 
    def __init__(self, type):
        # possede un type de lecteur (VHR, DVD, Blu-ray)
        self.type = type


    def play(self, film):
        print(f"Playing {film.title} ({film.year}), directed by {film.director} on a {self.color} player.")

    def stop(self):
        print(f"Stopping the player.")

    def eject(self):
        print(f"Ejecting the tape from the player.")