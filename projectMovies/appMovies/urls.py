from . import views
from django.urls import path
app_name = 'appMovies'

urlpatterns = [
        path('',views.home, name='home'),
        path('model_movies/<int:movie_id>/', views.details, name='details'),
        path('add_movies',views.add_movies, name="add_movies"),
        path('update/<int:id>/',views.update_movies, name="update_movies"),
        path('delete_movies/<int:id>/',views.delete_movies, name="delete_movies")
]