
"""Définit les films.

Note: l'utilisation de l'héritage ici est surtout à but éducatif.
"""


class Film:
    def __init__(self, title, date):
        self.title = title
        self.location = None
        self.date = date

    def __str__(self):
        return f"{self.title} ({self.date}), directed by {self.director}"

    def __repr__(self) -> str:
        return str(self)
class FilmVHR(Film):
    def __init__(self, title, date):
        super().__init__(title, date)

    def __str__(self):
        return f"{super().__str__()} - Format: VHS"

    
    def __repr__(self) -> str:
        return str(self)
    
class FilmDVD(Film):
    def __init__(self, title, date):
        super().__init__(title, date)

    def __str__(self):
        return f"{super().__str__()} - Format: DVD"

    def __repr__(self) -> str:
        return str(self)