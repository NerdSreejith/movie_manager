from . import views
from django.urls import path,include

urlpatterns = [
    
    path('',views.list_movies,name='index'), 
    path('list/',views.list_movies,name="list"),
    path('create/',views.create,name="create"),
    path('edit/<pk>',views.edit,name="edit"),
     path('delete/<pk>',views.delete,name="delete"),
    path('register/',views.register,name="register"),

]