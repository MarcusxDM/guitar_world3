from django.shortcuts import render

def search_index(request):
    return render(request, "index.html")

def search_form(request):
    # request_params = request.GET.copy()
    genre = request['genre']
    level = request['level']
    price = request['price']
    loud = request['loud']
    print(genre, level, price, loud)
    context = {'genre': genre}
    return render(request, 'results.html', context)

