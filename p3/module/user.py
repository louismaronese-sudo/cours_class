"""Classe représentant un utilisateur du système de contact."""


class User:
    """Un utilisateur."""

    def __init__(self, name, contact_method):
        """Initialise un nom et une méthode de contact."""
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        """Envoie un message via le système de contact de l'utilisateur."""
        self.contact_method.send(message)
