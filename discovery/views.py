from django.shortcuts import render

def search_index(request):
    return render(request, "index.html")