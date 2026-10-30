class User:
    """Un utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom et le mot de passe."""
        if len(username) < 2:
            raise UsernameTooShortException("erreurmaggle")
        if len(password) < 10:
            raise PasswordTooShortException()

        self.username = username
        self.password = password


class UsernameTooShortException(Exception):
    """Erreur sur le nom d'utilisateur."""

    def __init__(self, msg="", *args, **kwargs):
        """Init le message."""
        msg = msg or "Le nom d'utilisateur est trop court !"
        super().__init__(msg, *args, **kwargs)


class PasswordTooShortException(Exception):
    """Erreur sur le mot de passe."""

    def __init__(self, msg="", *args, **kwargs):
        """Init le message."""
        msg = msg or "Le mot de passe est trop court !"
        super().__init__(msg, *args, **kwargs)



def main():
    """Teste la création d'utilisateurs avec des données incorrectes."""
    
    # --- Test 1 : Nom d'utilisateur trop court ---
    print("--- Test 1 : Nom d'utilisateur trop court ---")
    try:
        # "A" fait 1 seul caractère, ce qui déclenche UsernameTooShortException
        user1 = User("A", "motdepassevalide123")
    except (UsernameTooShortException, PasswordTooShortException) as error:
        print(f"Erreur interceptée : {error}")

    # --- Test 2 : Mot de passe trop court ---
    print("\n--- Test 2 : Mot de passe trop court ---")
    
    try:
          # Le mot de passe fait moins de 10 caractères, déclenche PasswordTooShortException
          user2 = User("Alice", "12345")
    except (UsernameTooShortException, PasswordTooShortException) as error:
          print(f"Erreur interceptée : {error}")

    # --- Test 2.2: Mot de passe et nom trop courts---

    print("\n--- Test 2.2: Mot de passe trop court ---")
    try:
          # Le mot de passe fait moins de 10 caractères, déclenche PasswordTooShortException
          user2 = User("A", "12345")
    except (UsernameTooShortException, PasswordTooShortException) as error:
          print(f"Erreur interceptée : {error}")
  
    # --- Test 3 : Création valide (pour l'exemple) ---
    print("\n--- Test 3 : Utilisateur valide ---")
    try:
        user3 = User("Alice", "mon_super_mot_de_passe")
        print(f"Succès ! L'utilisateur '{user3.username}' a été créé avec succès.")
    except (UsernameTooShortException, PasswordTooShortException) as error:
        print(f"Erreur : {error}")


if __name__ == "__main__":
    main()