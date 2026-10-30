"""Point d'entrée de l'exemple de gestion des contacts."""

from module import OwlContactSystem, TextContactSystem, User, send_mass_messages


def main():
    """Envoie deux messages personnalisés aux utilisateurs."""
    alice = User("Alice", TextContactSystem("0102030405"))
    bob = User("Bob", OwlContactSystem("4 Privet Drive"))

    users = [alice, bob]
    send_mass_messages("Hello {name}, Comment vas-tu?", users)
    send_mass_messages(
        "Salut {name}. Tes informations de contact sont-elles correctes?"
        " Nous avons celles-ci: {contact_info}.",
        users,
    )


if __name__ == "__main__":
    main()