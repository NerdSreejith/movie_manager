from django.shortcuts import render, redirect
from .models import movies
from .forms import MovieForm
from .forms import UserForm
from django.contrib.auth.models import User
def create(request):
    frm = MovieForm()  # Instantiate an empty form
    if request.method == "POST":
        frm = MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('/list')
       
    return render(request, 'create.html', {'frm': frm})

def edit(request,pk):
    instance_edit = movies.objects.get(pk=pk)
    if request == 'POST':
        frm = MovieForm(request.POST,instance=instance_edit)
        if frm.is_valid:
            instance_edit.save()
    else:
            frm = MovieForm(instance=instance_edit)  
    return render(request, 'create.html',{'frm':frm})

def delete(request,pk):
    instance = movies.objects.get(pk=pk)
    instance.delete()
    return redirect('list')
    
def list_movies(request):
    movies_set = movies.objects.all()
    return render(request, 'list.html', {'movies': movies_set})


def register(request):
    form = UserForm()  # Instantiate the form
    if request.method == 'POST':  # Correcting the typo
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    return render(request, 'register.html', {'form': form})  #
