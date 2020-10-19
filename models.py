from django.db import models


class ImdbActor(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    about = models.TextField()
    dob = models.DateField()
    image = models.CharField(max_length=100)
    likes_on_fb = models.IntegerField()
    gender = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'IMDB_actor'


class ImdbCast(models.Model):
    role = models.CharField(max_length=100)
    is_debut_movie = models.BooleanField()
    remuneration = models.IntegerField()
    actor = models.ForeignKey(ImdbActor, models.DO_NOTHING)
    movie = models.ForeignKey('ImdbMovie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'IMDB_cast'


class ImdbDirector(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    remuneration = models.IntegerField()
    is_debut_movie = models.BooleanField()
    likes_on_fb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'IMDB_director'


class ImdbGenre(models.Model):
    type = models.CharField(max_length=101)

    class Meta:
        managed = False
        db_table = 'IMDB_genre'


class ImdbMovie(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    about = models.TextField()
    release_date = models.DateField()
    budget = models.IntegerField()
    collections = models.IntegerField()
    poster = models.CharField(max_length=100)
    dubbed_from = models.CharField(max_length=100)
    likes_on_fb = models.IntegerField()
    num_user_for_reviews = models.IntegerField()
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    average_rating = models.FloatField()
    lang = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'IMDB_movie'


class ImdbMovieDirectors(models.Model):
    movie = models.ForeignKey(ImdbMovie, models.DO_NOTHING)
    director = models.ForeignKey(ImdbDirector, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'IMDB_movie_directors'
        unique_together = (('movie', 'director'),)


class ImdbMovieGenres(models.Model):
    movie = models.ForeignKey(ImdbMovie, models.DO_NOTHING)
    genre = models.ForeignKey(ImdbGenre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'IMDB_movie_genres'
        unique_together = (('movie', 'genre'),)


class ImdbRating(models.Model):
    rating_one_count = models.IntegerField()
    rating_two_count = models.IntegerField()
    rating_three_count = models.IntegerField()
    rating_four_count = models.IntegerField()
    rating_five_count = models.IntegerField()
    movie = models.OneToOneField(ImdbMovie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'IMDB_rating'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
