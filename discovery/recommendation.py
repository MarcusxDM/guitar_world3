# -*- coding: utf-8 -*-
from owlready2 import *


if __name__ == '__main__':
    onto = get_ontology("file://Onto2.owl").load()
    new_user = onto.User("Marcus")

    # Level
    amateur = onto.Level("Amador")
    medium = onto.Level("Mediano")
    pro = onto.Level("Profissional")

    # Guitar
    les_paul = onto.Guitar("Les Paul")
    sg = onto.Guitar("SG")
    semi = onto.Guitar("Semi-Acustica")
    ibanez = onto.Guitar("Ibanez Grg")

    # Genre
    rock = onto.Genre("Rock")
    rock2 = onto.Genre("Rock")
    jazz = onto.Genre("Jazz")
    metal = onto.Genre("Metal")

    # Relate
    les_paul.has_genre = [rock]
    les_paul.has_genre.append(metal)
    les_paul.has_level = [amateur]
    ibanez.has_genre = [metal]
    semi.has_genre = [jazz]

    ibanez.color = ['Amarelo']
    les_paul.color = ['Amarelo']
    ibanez.loud = [True]
    les_paul.loud = [True]
    new_user.likes = [rock]
    # sync_reasoner()
    print(rock == rock2)
    print(ibanez.color == les_paul.color)
    print(ibanez.loud == les_paul.loud)
    print(new_user.recommendGuitar, rock.has_guitar, les_paul.has_genre, les_paul.has_level)
