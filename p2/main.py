from solutions.p2c4_forum import ImageFile, Moderator, User


def main():
    """Exécute un exemple de discussion et de modération."""
    user = User("John", "superpassword")
    moderator = Moderator("Lucie", "helloworld")

    thread = user.make_thread(
        "Gâteau à la vanille",
        "Vous aimez les gâteaux à la vanille ?",
    )
    moderator.post(thread, "Oui, j'aime beaucoup !")
    thread.display()


    off_topic_post = user.post(thread, "Et vous aimez les voitures ?")
    moderator_reply = moderator.post(thread, "Ce message est hors sujet.")
    thread.display()

    print("Le modérateur supprime les deux messages hors sujet.")
    moderator.delete(thread, off_topic_post)
    moderator.delete(thread, moderator_reply)
    thread.display()


    image = ImageFile(name="image de gâteau", size=3)
    user.post(thread, "Voici une image de mon gâteau !", file=image)
    moderator.post(thread, "Il a l'air délicieux !")
    thread.display()


if __name__ == "__main__":
    main()