"""Classe abstraite et implémentations des systèmes de contact."""

from abc import ABC, abstractmethod

from .validators import validate_phone, varify_address


class ContactSystem(ABC):
    """Classe abstraite utilisée pour envoyer un message à un utilisateur."""

    @abstractmethod
    def send(self, message):
        """Toutes les sous-classes de ContactSystem doivent implémenter send."""
        pass


class TextContactSystem(ContactSystem):
    """Envoie un message à l'utilisateur par SMS."""

    def __init__(self, phone_number):
        """Initialise le numéro de téléphone."""
        super().__init__()
        validate_phone(phone_number)
        self.phone_number = phone_number

    def send(self, message):
        """Envoie le message."""
        print(f'Envoi du message "{message}" au numéro {self.phone_number}')

    def __str__(self):
        """Retourne une représentation lisible."""
        return f"Le numéro de téléphone est {self.phone_number}"


class OwlContactSystem(ContactSystem):
    """Envoie un message en utilisant une chouette."""

    def __init__(self, address):
        """Initialise l'adresse."""
        varify_address(address)
        self.address = address
        self.owl = "Hedwige"
        super().__init__()

    def send(self, message):
        """Envoie le message."""
        print(f'Envoi du message "{message}" par chouette {self.owl}')

    def __str__(self):
        """Retourne une représentation lisible."""
        return f"L'adresse est '{self.address}'"
