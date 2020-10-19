
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name='imdb_app'
urlpatterns = [
    path('',views.homepage),
    path('home/',views.homepage),
    path('movie/<str:movie_id>/',views.movie_page),
    path('movie/',views.movies_homepage),
    path('actor/<str:actor_id>/',views.actor_page),
    path('director/<str:director_id>/',views.director_page),
    path('analytics/',views.analytics_page)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

