from django.shortcuts import render, redirect
from .models import movies

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        year = request.POST.get('year')
        desc = request.POST.get('description') 
        movie_obj = movies.objects.create(title=title, year=year, description=desc)
        movie_obj.save()
        return redirect('/list')
    return render(request, 'create.html')

def edit(request):
    # Add your edit logic here
    return render(request, 'edit.html')

def list_movies(request):
    movies_set = movies.objects.all()
    return render(request, 'list.html', {'movies': movies_set})
