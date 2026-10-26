from solutions.p1c4_toolbox import *


# Instanciez une boîte à outils, un tournevis, et un marteau.
hammer = Hammer()
screwdriver = Screwdriver()
toolbox = ToolBox()

# Placez le marteau et le tournevis dans la boîte à outils.
toolbox.add_tool(hammer)
toolbox.add_tool(screwdriver)

# Instanciez une vis, et serrez-la avec le tournevis.
# Affichez la vis avant après avoir été serrée.
screw = Screw()
print(screw)
screwdriver.tighten(screw)
print(screw)

# Instanciez un clou, puis enfoncez-le avec le marteau.
# Affichez le clou avant et après avoir été enfoncé.
nail = Nail()
print(nail)
hammer.hammer_in(nail)
print(nail)


# --------------------------------------------------------------
# Que pouvez-vous faire d’autre avec ces classes et ces objets ?

# enlever un outil
print("outils dans la boîte:", toolbox.tools)
toolbox.remove_tool(hammer)
print("on a enlevé le marteau")
print("outils dans la boîte:", toolbox.tools)

# désserrer la vis
screwdriver.loosen(screw)
print(screw)

# enlever le clou
hammer.remove(nail)
print(nail)

# repeindre le marteau
hammer.paint("yellow")
print(hammer)
