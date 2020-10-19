import os

from .models import *

test_data_path = os.path.join(os.path.dirname(__file__), 'sample_data')

def get_one_bar_plot_data(title=None,labels=None,data=None):
    import json
    single_bar_chart_data = {
        "labels": labels,
        "datasets":
    [
        {
        "label": " ",
        "data": data,
        "name": "Single Bar Chart",
        "borderColor": "rgba(0, 123, 255, 0.9)",
        "border_width": "0",
        "backgroundColor": ["rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)","rgb(204, 153, 0)","rgb(102, 255, 51)","rgb(51, 204, 255)"]
    }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': title
    }


def get_two_bar_plot_data(title=None,labels=None,data1=None,data2=None):
    import json
    multi_bar_plot_data = {
        "labels": labels,
        "datasets": [
            {
                "label": "Budget",
                "data": data1,
                "borderColor": "green",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "Collections",
                "data": data2,
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.09)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': title
    }


def get_multi_line_plot_data(title=None,labels=None,data1=None,data2=None):
    import json
    multi_line_plot_data = {
        "labels": labels,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Male",
            "data": data1,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Female",
            "data": data2,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': title
    }


def get_area_plot_data(title=None,data=None,labels=None):
    import json
    area_plot_data = {
        "labels": labels,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": data,
            "label": "Expense",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': title+' Movie Graph '
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": sub_title_2,
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": sub_title_2,
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'radar Chart'
    }


def get_doughnut_chart_data(title=None,labels=None,data=None):
    import json
    doughnut_graph_data = {
        "datasets": [{
            "data": data,
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels":labels
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': title
    }


def get_multi_line_plot_with_area_data(title=None,labels=None,data1=None,data2=None,sub_title_1=None,sub_title_2=None):
    import json
    multi_line_plot_with_area_data = {
        "labels":labels,
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label":sub_title_1,
                "borderColor": "black",
                "borderWidth": "1",
                "backgroundColor": "black",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": data1
            },
            {
                "label": sub_title_2,
                "borderColor": "green",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.17)",
                "data": data2
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': title
    }


def get_pie_chart_data(title=None,labels=None,data=None):
    import json

    pie_chart_data = {
        "datasets": [{
            "data": data,
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": labels
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': title
    }


def get_polar_chart_data():
    import json

    polar_chart_data = {
        "datasets": [{
            "data": [15, 18, 9, 6, 19],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4",
            "Green5"
        ]
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'polar Chart Data'
    }


def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows


def sql(query):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    output=[]
    for index in range(len(rows)):
        output.append(rows[index][0])
    return output

def get_average_rating_of_movie(movie_obj):
    try:
        rating=Rating.objects.filter(movie=movie_obj).values_list()[0]
        sum_of_ratings=rating[2]*1+rating[3]*2+rating[4]*3+rating[4]*4+rating[6]*5
        no_of_ratings=rating[2]+rating[3]+rating[4]+rating[5]+rating[6]
        average = sum_of_ratings/no_of_ratings
    except (IndexError,ZeroDivisionError) as e:
        average=0
    return round(average,1)



import json
with open(os.path.join(test_data_path,'actors_100.json')) as f:
    data = json.load(f)
actors_list=data
with open(os.path.join(test_data_path,'directors_100.json')) as f:
    data = json.load(f)
directors_list=data
with open(os.path.join(test_data_path,'movies_100.json')) as f:
    data = json.load(f)
movies_list=data






def populate_database(actors_list=None,movies_list=None, directors_list=directors_list, movie_rating_list=None):
# populate_database(movies_list=mov)
    if actors_list :
        for each_actor in actors_list:
            Actor.objects.create(
                id=each_actor['actor_id'],
                gender=each_actor['gender'],
                name=each_actor['name'],
                likes_on_fb=each_actor['fb_likes'],

                )
            
    if directors_list:
        for each_director in directors_list:
            director_obj=Director.objects.create(
                name=each_director['name'],
                gender=each_director['gender'],
                likes_on_fb=each_director['no_of_facebook_likes']
                )

    if movies_list:
        for each_movie in movies_list:
            actor_list=each_movie.get('actors')
            # director_list=each_movie.get('director_name')
            genres_list=each_movie.get('genres')
            director_obj=Director.objects.filter(name=each_movie['director_name'])[0]
            movie_obj=Movie.objects.create(
                    id=each_movie['movie_id'],
                    name=each_movie['name'],
                    # release_date=each_movie['year_of_release'],
                    collections=each_movie['box_office_collection_in_crores'],
                    budget=each_movie['budget'],
                    release_date=each_movie['year_of_release'],
                    country=each_movie['country'],
                    language=each_movie['language'],
                    average_rating=each_movie['average_rating'],
                    num_user_for_reviews=each_movie['num_user_for_reviews']
                    )
            movie_obj.directors.add(director_obj)
            for each_actor in actor_list:
                try:
                    actor_obj = Actor.objects.get(
                    id=each_actor['actor_id'])
                except Actor.DoesNotExist:
                    ""
                cast=Cast.objects.create(
                    actor=actor_obj,
                    movie=movie_obj,
                    role=each_actor['role'],
                    is_debut_movie=each_actor['is_debut_movie']
                    )
            for each_genre in genres_list:
                try:
                    movie_obj=Movie.objects.get(id=each_movie['movie_id'])
                except Movie.DoesNotExist:
                    ""

                try:
                    genre_obj=Genre.objects.get(type=each_genre)
                except Genre.DoesNotExist as e:
                    genre_obj=Genre.objects.create(type=each_genre)

                movie_obj.genres.add(genre_obj)
    
            
    if movie_rating_list:
        for each_movie in movie_rating_list:
            movie_obj=Movie.objects.get(id=each_movie['movie_id'])
            rating_obj=Rating.objects.create(
                movie=movie_obj,
                rating_one_count=each_movie['rating_one_count'],
                rating_two_count=each_movie['rating_two_count'],
                rating_three_count=each_movie['rating_three_count'],
                rating_four_count=each_movie['rating_four_count'],
                rating_five_count=each_movie['rating_five_count']
                )
