from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core import serializers
from .models import *
from .utils import *

# Create your views here.
def homepage(request):
    movies = Movie.objects.order_by('-release_date')[:10]
    # movies=Movie.objects.all()
    directors=[]
    rating=[]
    genres=[]
    for movie in movies:
        directors.append(movie.directors.all())
        rating.append(get_average_rating_of_movie(movie))
        genres.append(Genre.objects.filter(movie=movie))
    return render(request,'imdb_home.html',{'check':movies,'movies':zip(movies,directors,rating,genres)})

def movies_homepage(request):
    movies=Movie.objects.filter()
    return render(request,'movies_home.html',{'movies':movies})

def movie_page(request,movie_id):
    movie=Movie.objects.filter(pk=movie_id)[0]
    directors=Director.objects.filter(movie=movie_id)
    cast= Cast.objects.filter(movie__id=movie_id)
    actors=Actor.objects.filter(cast__movie__id=movie_id).distinct()
    roles=[]
    for actor in actors:
        roles.append(Cast.objects.filter(actor=actor,movie=movie))
    return render(request,'imdb_movie.html',{'movie':movie,'directors':directors,'cast':zip(cast,roles,actors)})


def actor_page(request,actor_id):
    actor=Actor.objects.filter(id=actor_id)[0]
    movies=Movie.objects.filter(actors__id=actor_id).distinct()
    rating=[]
    Remuneration=[]
    for movie in movies:
        sum=0
        for each_role in Cast.objects.filter(actor=actor):
            sum+=each_role.remuneration
        Remuneration.append(sum)
    for movie in movies:
        rating.append(get_average_rating_of_movie(movie))
    return render(request,'imdb_actor.html',{'actor':actor,'check':movies, 'movies':zip(movies,rating,Remuneration)})

def director_page(request,director_id):
    director=Director.objects.filter(id=director_id)[0]
    movies=Movie.objects.filter(directors=director)
    rating=[]
    for movie in movies:
        rating.append(get_average_rating_of_movie(movie))
    return render(request,'imdb_director.html',{'check':director,'movies':zip(movies,rating),'director':director})

def analytics_page(request):

    data={}
     #1 Genre vs Rating
    genres=list(Genre.objects.all().values_list('type',flat=True))
    
    movies=list(Movie.objects.filter().values_list('id',flat=True).distinct())#release_date__year__gte=2000,release_date__year__lte=2020
    rating_sum=0
    for movie in movies:
        rating_sum+=Movie.objects.filter(id=movie).values_list('average_rating',flat=True)[0]
    try:
        average=rating_sum/len(movies)
    except ZeroDivisionError as e:
        average=0
    rating=[]
    for movie in movies:
        if Movie.objects.filter(id=movie).values_list('average_rating',flat=True)[0]>average:
            rating.append(Movie.objects.filter(id=movie).values_list('average_rating',flat=True)[0])

    data.update(get_one_bar_plot_data('Which Genre attracting people Most',genres,rating))
    
    


    #2 Year Wise Male vs Female
    query="select count(a.gender) as Count,strftime('%Y',m.release_date) Year from IMDB_actor as a JOIN IMDB_cast as c ON a.id=c.actor_id JOIN IMDB_movie as m ON  m.id=c.movie_id group by a.gender,strftime('%Y',m.release_date) having a.gender='M'" 
    males=sql(query)
    query="select count(a.gender) as Count,strftime('%Y',m.release_date) Year from IMDB_actor as a JOIN IMDB_cast as c ON a.id=c.actor_id JOIN IMDB_movie as m ON  m.id=c.movie_id group by a.gender,strftime('%Y',m.release_date) having a.gender='F'" 
    females=sql(query)
    query="select strftime('%Y',m.release_date) Year from IMDB_movie m group by Year" 
    years=sql(query)

    data.update(get_multi_line_plot_data('Male vs Female Actors growth in Industry',years,males,females))


    #3 Average Budget vs Collections Year Wise
    query="select avg(m.budget) Budget from IMDB_movie m group by strftime('%Y',m.release_date);"
    avg_budgets=sql(query)
    query="select avg(m.collections) Collections from IMDB_movie m group by strftime('%Y',m.release_date)"
    avg_collections=sql(query)
    query="select strftime('%Y',m.release_date) Year from IMDB_movie m group by Year" 
    years=sql(query)
    data.update(get_two_bar_plot_data('Year wise Budget vs Collections in industry',years,avg_budgets,avg_collections))

    #4 Dubbed Movies vs Normal Movies
    average_collections=sql('SELECT AVG(Collections) FROM IMDB_movie')
    query="SELECT COUNT(id) FROM IMDB_movie m where dubbed_from!='NA' AND collections>=(SELECT AVG(collections) FROM IMDB_movie) group by strftime('%Y',m.release_date)"
    dubbed_movies=sql(query)
    query="SELECT COUNT(id) FROM IMDB_movie m where dubbed_from='NA' AND collections>=(SELECT AVG(collections) FROM IMDB_movie) group by strftime('%Y',m.release_date)"
    normal_movies=sql(query)
    query="select strftime('%Y',m.release_date) Year from IMDB_movie m group by Year" 
    years=sql(query)
    data.update(get_multi_line_plot_with_area_data('Normal Movies vs Dubbed Movies Growth',years,normal_movies,dubbed_movies,' Movies','Dubbed_Movies'))  
    return render(request,'analytics.html',data)