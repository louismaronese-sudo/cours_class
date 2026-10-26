from solutions.p2c4_forum import *
from solutions.p1c4_toolbox import *

class Person:
    """Personne."""

    def __init__(self, name, agecoucou):
        """Donne un nom."""
        self.name = name
        self.age = agecoucou
    
    def walk(self):
        """Marche."""
        print(f"{self.name} marche. Pas mal pour son âge de {self.age} an" + ("s" if self.age > 1 else "") + ".")

volunteers = [Person("Alice", 1), Person("Bob", 25), Person("Carol", 35)]
for volunteer in volunteers:
    volunteer.walk()


# Ici, nous reprenons nos outils !

myhammer = Hammer("blue")
myscrewdriver = Screwdriver(5)    

toolbox = {
    "screwdriver": myscrewdriver, 
    "hammer": myhammer,
    "nailss": [Nail(),Nail(),Nail()],
    "screws": [Screw(),Screw()]
}
print("Outils dans la boîte:", toolbox)

# 1. Enfoncer le 1er clou (index 0)
toolbox["nailss"][0].nail_in()

# 2. Retirer le 3ème clou (index 2)
toolbox["nailss"][2].remove()
toolbox["screws"][1].tighten()
myhammer.paint("yellow")
# Vérification
print("Outils mis à jour:", toolbox)

class Lion():
    """Lion."""

    def __init__(self, name):
        """Initialise le nom du lion."""
        self.name = name

    def action(self):
        """Fait rugir le lion."""
        print(f"{self.name} rugit !")

class Human():
    """Humain."""

    def __init__(self, name):
        """Initialise le nom de l'humain."""
        self.name = name

    def action(self):
        """Fait parler l'humain."""
        print(f"{self.name} parle !")

class Fish():
    """Poisson."""

    def __init__(self, name):
        """Initialise le nom du poisson."""
        self.name = name

    def swim(self):
        """Fait nager le poisson."""
        print(f"{self.name} nage !")

Liste = [Lion("Simba"),Human("Alice"), Fish("Nemo")]

for entities in Liste:
    if isinstance(entities, Fish):
        entities.swim()
    else:
        entities.action()