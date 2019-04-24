from django.shortcuts import render, redirect


def search_index(request):
    return render(request, "index.html")

def results(request):
    # request_params = request.GET.copy()
    if request.method=='POST':
        genre = request.POST['genre']
        level = request.POST['level']
        price = request.POST['price']
        loud = request.POST['loud']
        color = request.POST['color']
        chords = request.POST['chords']
        print(genre, level, price, loud)
        context = {'genre': genre}
        # ('/admin')
    return render(request, 'results.html', context)

