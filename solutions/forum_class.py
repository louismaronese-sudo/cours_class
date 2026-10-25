from datetime import datetime

# ==========================================
# 1. HIÉRARCHIE DES UTILISATEURS
# ==========================================

class Utilisateur:
    """Classe parent représentant un utilisateur standard du forum."""
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def se_connecter(self):
        print(f"{self.nom} s'est connecté au forum.")

    def creer_fil(self, titre):
        """Crée un nouveau fil de discussion."""
        return FilDeDiscussion(titre)

    def publier_post(self, fil, texte):
        """Ajoute un post standard dans un fil."""
        post = Post(texte, self)
        fil.posts.append(post)
        return post


class Moderateur(Utilisateur):
    """Classe enfant : un modérateur est un utilisateur avec des droits étendus."""
    
    def modifier_post(self, post, nouveau_texte):
        """Modifie le contenu d'un post."""
        post.texte = nouveau_texte
        print(f"[Modération] Le post a été modifié par {self.nom}.")

    def supprimer_post(self, post, fil):
        """Supprime un post s'il ne respecte pas les règles."""
        if post in fil.posts:
            fil.posts.remove(post)
            print(f"[Modération] Le post a été supprimé par {self.nom}.")


# ==========================================
# 2. GESTION DES FILS DE DISCUSSION & POSTS
# ==========================================

class FilDeDiscussion:
    """Représente un fil de discussion."""
    def __init__(self, titre):
        self.titre = titre
        self.date_creation = datetime.now()
        self.posts = []


class Post:
    """Classe parent représentant un post classique."""
    def __init__(self, texte, auteur):
        self.texte = texte
        self.auteur = auteur
        self.date_publication = datetime.now()

    def afficher(self):
        print(f"[{self.auteur.nom}] - {self.date_publication.strftime('%H:%M')} :\n{self.texte}\n")


class PostAvecFichier(Post):
    """Classe enfant : un post contenant un fichier (ex: image de gâteau)."""
    def __init__(self, texte, auteur, nom_fichier):
        super().__init__(texte, auteur) # Récupère les attributs du Post de base
        self.nom_fichier = nom_fichier

    def afficher(self):
        """Redéfinit l'affichage pour intégrer le fichier attaché."""
        print(f"[{self.auteur.nom}] - {self.date_publication.strftime('%H:%M')} :\n{self.texte}")
        print(f"📎 [Fichier joint : {self.nom_fichier}]\n")