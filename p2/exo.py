from solutions.mes_class import ToolBox, Screwdriver, Hammer, Screw, Nail
from solutions.mes_class_sousclass import Film, Player


Monjoueur = Player("VHR")
#Creation de ma boite a outil et de mes 2 outils
mytoolbox = ToolBox()
myscrewdriver = Screwdriver(5)
myhammer = Hammer("blue")

#voila ce que je possede
print(f"J'ai comme outils un marteau : {myhammer.color} et un tournevis de taille : {myscrewdriver.size}")
print(mytoolbox.tools)

#j'ajoute mes outils a ma boite a outil
mytoolbox.add_tool(myhammer)
mytoolbox.add_tool(myscrewdriver)   
print(mytoolbox.tools)

#je crée une vis et un clou
myscrew = Screw()
mynail = Nail()
print(f"J'ai une vis : {myscrew} et un clou : {mynail}")

#je serre ma vis avec mon tournevis
myscrewdriver.tighten(myscrew)
print(f"J'ai une vis : {myscrew} avec un serrage de {myscrew.tightness}")

#je place mon clou dans le mur avec mon marteau
myhammer.hammer_in(mynail)
print(f"J'ai un clou : {mynail} ")

#enleve le clou du mur avec mon marteau
myhammer.remove(mynail)
print(f"j' ai a present : {mynail} ")

#repreindre mon marteau en rouge
myhammer.paint("red")
print(f"J'ai un marteau : {myhammer.color}")

#enleve mon marteau de ma boite a outil
mytoolbox.remove_tool(myhammer)
print(mytoolbox.tools)
myhammer.hammer_in(mynail)
print(f"j' ai a present : {mynail} ")
