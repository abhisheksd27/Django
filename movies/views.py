from django.http import HttpResponse , HttpResponseRedirect,Http404
from django.shortcuts import render
from .models import Movie


# data= {
#     'movies' : [
#         {
#             'id':5,
#             "title": "Jaws",
#             'Year': 1988
#         },
#         {
#             'id':5,
#             "title": "avengers",
#             'Year': 2018 
#         },
#         {
#              'id':6,
#             "title": "Spidermanb",
#             'Year': 2022
#         }
#     ]
# }
def movies(request):
    data = Movie.objects.all()
    
    return render(request , 'movies/movies.html', {'movies' :data})


def Home(request):
    return HttpResponse("home page")


def detail(request,id):
    data= Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html' ,{'movie':data})


def add(request):
    title=request.POST.get('title')
    year =request.POST.get('year')
    if title and year:
        movie= Movie(title=title,year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    
    
    return render(request , 'movies/add.html')


def delete(request,id):
    try:
        data= Movie.objects.get(pk=id)
    except:
        raise Http404('Movies  does not exist')
    data.delete()
    return HttpResponseRedirect('/movies')
    