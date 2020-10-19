def populate_database(actors_list=None, movies_list=None, directors_list=None, movie_rating_list=None):
    
    if actors_list :
        for each_actor in actors_list:
            Actor.objects.create(actor_id=each_actor['actor_id'],name=each_actor['name'])
            
    if directors_list:
        for each_director in directors_list:
            director_obj=Director.objects.create(name=each_director)

    if movies_list:
        for each_movie in movies_list:
            actors_list=each_movie.get('actors')
            director_obj=Director.objects.get(name=each_movie['director_name'])
            movie_obj=Movie.objects.create(
                    name=each_movie['name'],
                    movie_id=each_movie['movie_id'],
                    release_date=each_movie['release_date'],
                    box_office_collection_in_crores=each_movie['box_office_collection_in_crores'],
                    director=director_obj
                    )
            
            for each_actor in actors_list:
                actor_obj = Actor.objects.get(actor_id=each_actor['actor_id'])
                cast=Cast.objects.create(
                    actor=actor_obj,
                    movie=movie_obj,
                    role=each_actor['role'],
                    is_debut_movie=each_actor['is_debut_movie']
                    )
    
            
    if movie_rating_list:
        for each_movie in movie_rating_list:
            movie_obj=Movie.objects.get(movie_id=each_movie['movie_id'])
            rating_obj=Rating.objects.create(
                movie=movie_obj,
                rating_one_count=each_movie['rating_one_count'],
                rating_two_count=each_movie['rating_two_count'],
                rating_three_count=each_movie['rating_three_count'],
                rating_four_count=each_movie['rating_four_count'],
                rating_five_count=each_movie['rating_five_count']
                )