from django.db import models

# Create your models here.

class Movie(models.Model):
    id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(default=' ',max_length=100)
    about=models.TextField(default=' ')
    directors=models.ManyToManyField('Director')
    actors=models.ManyToManyField('Actor',through='Cast')
    release_date=models.DateField()
    budget=models.IntegerField(default=0)
    collections=models.IntegerField(default=1)
    poster=models.ImageField(default='DilLip.jpg')
    genres=models.ManyToManyField('Genre')
    lang_choices=(
        ('Telugu','Telugu'),
        ('Tamil','Tamil'),
        ('Kannada','Kannada'),
        ('Hindi','Hindi'),
        ('English','English'),
        ('NA','Not Dubbed')
    )
    lang=models.CharField(max_length=100,choices=lang_choices)#default='Tel'
    dubbed_from=models.CharField(max_length=100,choices=lang_choices)
    likes_on_fb=models.IntegerField(default=0)
    num_user_for_reviews=models.IntegerField(default=0)
    country=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    average_rating=models.FloatField()

    def __str__(self):
    	return self.name

class Director(models.Model):
    name=models.CharField(default=' ',max_length=100)
    about=models.TextField(default=' ')
    image=models.ImageField(default='DilLip.jpg')
    gender_choices=(
        ('M','Male'),
        ('F','Female')
    )
    gender=models.CharField(default=' ',max_length=100,choices=gender_choices)
    remuneration=models.IntegerField(default=1,)
    is_debut_movie=models.BooleanField(default=False)
    likes_on_fb=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Actor(models.Model):
    id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(default=' ',max_length=100)
    about=models.TextField(default=' ')
    dob=models.DateField(default='2020-03-03')
    image=models.ImageField(default='Default.jpg')
    gender_choices=(
        ('M','Male'),
        ('F','Female')
    )
    gender=models.CharField(default=' ',max_length=100,choices=gender_choices)
    likes_on_fb=models.IntegerField(default=0)


    def __str__(self):
        return self.name
    

class Cast(models.Model):
    actor=models.ForeignKey('Actor',on_delete=models.CASCADE)
    movie=models.ForeignKey('Movie',on_delete=models.CASCADE)
    role=models.CharField(default=' ',max_length=100)
    is_debut_movie=models.BooleanField(default=False)
    remuneration=models.IntegerField(default=1,)
    

class Rating(models.Model):
    movie=models.OneToOneField(Movie,on_delete=models.CASCADE)#primary_key=True
    rating_one_count=models.IntegerField(default=0)
    rating_two_count=models.IntegerField(default=0)
    rating_three_count=models.IntegerField(default=0)
    rating_four_count=models.IntegerField(default=0)
    rating_five_count=models.IntegerField(default=0)

    def __str__(self):
        return self.movie.name


class Genre(models.Model):
    type=models.CharField(default=' ',max_length=101)
    def __str__(self):
        return self.type
    
    