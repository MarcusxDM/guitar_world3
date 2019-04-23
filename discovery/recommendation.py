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
    jazz = onto.Genre("Jazz")
    metal = onto.Genre("Metal")


    les_paul.has_genre = [rock]
    les_paul.has_level = [amateur]
    ibanez.has_genre = [metal]
    semi.has_genre = [jazz]

    new_user.likes = rock
    sync_reasoner()
    print(rock.has_guitar, les_paul.has_genre, les_paul.has_level)
