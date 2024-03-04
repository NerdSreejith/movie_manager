from . import views
from django.urls import path,include

urlpatterns = [
    
    path('',views.list_movies,name='index'), 
    path('list/',views.list_movies,name="list"),
    path('create/',views.create,name="create"),
    path('edit/',views.edit,name="edit"),
]