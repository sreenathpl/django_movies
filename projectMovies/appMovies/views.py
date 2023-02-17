from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import form_movies
from .models import model_movies

# Create your views here.
def home(request):
    movie = model_movies.objects.all()
    context = {'movies':movie}
    return render(request,'index.html', context)
    # return render(request,"index.html")
def details(request,movie_id):
    movie= model_movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})

def add_movies(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        cat = request.POST.get('cat')
        duration = request.POST.get('duration')
        director = request.POST.get('director')

        movie = model_movies(name = name,
                             desc = desc,
                             year = year,
                             img = img,
                             cat = cat,
                             duration = duration,
                             director = director)
        movie.save()
        return redirect('/')
    return render(request,'add_movies.html')

def update_movies(request, id):
    movie = model_movies.objects.get(id = id)
    form = form_movies(request.POST or None,
                       request.FILES,
                       instance = movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form, 'movie':movie})

def delete_movies(request, id):
    if request.method == "POST":
        movie = model_movies.objects.get(id= id)
        movie.delete()
        return redirect('/')
    return render(request,'delete_movies.html')