from solutions.mes_class_sousclass import *

film1 = Film("The Matrix",'1999')
film1.watch()

filmcassette1 = FilmCassette("Inception", '2010', "Christopher Nolan")
print(filmcassette1)
filmcassette1.rewind()
print(filmcassette1.magnetic_tape)