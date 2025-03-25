from django.urls import path
from . import views 

# Define as urls que serão usadas com as views
urlpatterns = [
    path('', views .listar_postagens, name= 'listar_posts'),
]
