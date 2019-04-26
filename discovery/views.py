from django.shortcuts import render, redirect
from owlready2 import *

GENRE_WEIGHT = 15
LEVEL_WEIGHT = 8
LOUD_WEIGHT = 5
COLOR_WEIGHT = 4
CHORDS_WEIGHT = 2


def db_guitar_init():
    onto = get_ontology("file://discovery/Onto2.owl").load()

    # Guitar
    les_paul = onto.Guitar("Les Paul")
    # sg = onto.Guitar("SG")
    semi = onto.Guitar("Semi-Acustica")
    ibanez = onto.Guitar("Ibanez Grg")
    g = onto.Guitar("Guitarra 1")
    g2 = onto.Guitar("Guitarra 2")
    g3 = onto.Guitar("Guitarra 3")
    g4 = onto.Guitar("Guitarra 4")
    g5 = onto.Guitar("Guitarra 5")

    # Genre
    rock = onto.Genre("Rock")
    jazz = onto.Genre("Jazz")
    metal = onto.Genre("Metal")

    # Level
    iniciante = onto.Level("Iniciante")
    amador = onto.Level("Amador")
    profissional = onto.Level("Profissional")

    # Relate
    les_paul.has_genre = [rock]
    les_paul.has_genre.append(metal)
    les_paul.price = [1000]
    les_paul.loud = [True]
    les_paul.color = ["Preto"]
    les_paul.chords = [0.9]
    les_paul.has_levelGuitar = [amador]

    ibanez.has_genre = [metal]
    ibanez.price = [900]
    ibanez.loud = [True]
    ibanez.color = ["Vermelho"]
    ibanez.chords = [0.11]
    ibanez.has_levelGuitar = [iniciante]

    semi.has_genre = [jazz]
    semi.price = [2000]
    semi.loud = [False]
    semi.color = ["Sunburst"]
    semi.chords = [0.10]
    semi.has_levelGuitar = [profissional]

    g.has_genre = [jazz]
    g.has_genre.append(metal)
    g.price = [1500]
    g.loud = [True]
    g.color = ["Preto"]
    g.chords = [0.11]
    g.has_levelGuitar = [profissional]

    g2.has_genre = [rock]
    g2.price = [500]
    g2.loud = [False]
    g2.color = ["Vermelho"]
    g2.chords = [0.9]
    g2.has_levelGuitar = [profissional]

    g3.has_genre = [metal]
    g3.price = [100]
    g3.loud = [True]
    g3.color = ["Sunburst"]
    g3.chords = [0.11]
    g3.has_levelGuitar = [iniciante]

    g4.has_genre = [jazz]
    g4.price = [1000]
    g4.loud = [True]
    g4.color = ["Preto"]
    g4.chords = [0.9]
    g4.has_levelGuitar = [amador]
    g4.has_levelGuitar.append(profissional)
    g4.has_levelGuitar.append(iniciante)

    g5.has_genre = [jazz]
    g5.price = [1800]
    g5.loud = [False]
    g5.color = ["Vermelho"]
    g5.chords = [0.9]
    g4.has_levelGuitar = [amador]
    g4.has_levelGuitar.append(profissional)

    db_guitar = [les_paul, semi, ibanez, g, g2, g3, g4, g5]

    return db_guitar


def onto_user(genre, level):
    onto = get_ontology("file://discovery/Onto2.owl").load()
    user = onto.User("Logged User")

    # Genre
    genre_onto = onto.Genre(genre)
    user.likes = [genre_onto]

    # Level
    level_onto = onto.Level(level)
    user.has_level = [level_onto]

    return user


def onto_guitar_perfect(price, loud, color, chords):
    onto = get_ontology("file://discovery/Onto2.owl").load()

    # Perfect Guitar
    perfect_guitar = onto.Guitar("Perfect_Guitar")
    perfect_guitar.price = [price]
    perfect_guitar.loud = [loud]
    perfect_guitar.color = [color]
    perfect_guitar.chords = [chords]
    # perfect_guitar.has_genre = [genre_onto]
    # perfect_guitar.has_level = level_onto

    return perfect_guitar


def similarity(user, perfect_guitar, guitar):
    result = 0
    print (perfect_guitar.name, perfect_guitar.loud, guitar.name, guitar.loud)
    if any(liked_genre in user.likes for liked_genre in guitar.has_genre):
        result += GENRE_WEIGHT
    if any(has_level in user.has_level for has_level in guitar.has_levelGuitar):
        result += LEVEL_WEIGHT
    if perfect_guitar.loud == guitar.loud:
        result += LOUD_WEIGHT
    if perfect_guitar.color == guitar.color:
        result += COLOR_WEIGHT
    if perfect_guitar.chords == guitar.chords:
        result += CHORDS_WEIGHT

    # if perfect_guitar.has_level = level_onto
    guitar.similarity = [result]
    return guitar


def search_index(request):
    return render(request, "index.html")


def results(request):
    # request_params = request.GET.copy()
    if request.method == 'POST':
        genre = request.POST['genre']
        level_post = request.POST['level']
        price = request.POST['price']
        loud = request.POST['loud']
        color = request.POST['color']
        chords = request.POST['chords']

        price = float(price)
        loud = (loud == '0')
        chords = float(chords)

        user = onto_user(genre, level_post)
        perfect_guitar = onto_guitar_perfect(price, loud, color, chords)
        recommended_guitar_list = []
        db_guitar = db_guitar_init()
        sync_reasoner()

        for guitar in db_guitar:
            similarity(user, perfect_guitar, guitar)
            if guitar.similarity[0] > 0 and guitar.price[0] <= price:
                recommended_guitar_list.append(guitar)

        recommended_guitar_list.sort(key=lambda x: x.similarity, reverse=True)

        print("\n\nRecommended guitars: ")
        for guitar in recommended_guitar_list:
            print (guitar.name, guitar.similarity[0], "points of similarity")

        context = {'recommended_guitar_list': recommended_guitar_list}
        # ('/admin')
    return render(request, 'results.html', context)
