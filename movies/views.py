from django.http import HttpResponse
from django.shortcuts import render


data= {
    'movies' : [
        {
            'id':5,
            "title": "Jaws",
            'Year': 1988
        },
        {
            'id':5,
            "title": "avengers",
            'Year': 2018 
        },
        {
             'id':6,
            "title": "Spidermanb",
            'Year': 2022
        }
    ]
}
def movies(request):
    return render(request , 'movies/movies.html', data)


def Home(request):
    return HttpResponse("home page")