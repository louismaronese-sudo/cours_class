from solutions.mes_class_sousclass import *

film1 = Film("The Matrix",'1999')

filmcassette1 = FilmCassette("Inception", '2010', "Christopher Nolan")
print(filmcassette1)
filmcassette1.rewind()
print(filmcassette1.magnetic_tape)
print(filmcassette1.title)

player1 = Player("DVD")
print(f"Player type: {player1.type}")   
filmcassette1.watch(player1)  # Should print a message indicating that the film cannot be watched on a DVD player

player2 = Player("VHR")
print(f"Player type: {player2.type}")
filmcassette1.watch(player2)  # Should print a message indicating that the film