
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('create/',views.create, name="create"),
    path('delete/<Todo_id>', views.delete,name="delete"),
    path('yes_finish/<Todo_id>', views.yes_finish,name="yes_finish"),
    path('no_finish/<Todo_id>', views.no_finish,name="no_finish"),
    path('update/<Todo_id>', views.update,name="update"),

]