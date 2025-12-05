from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home2/<str:name>/', views.home2, name='home2'),
    path('makeperson/', views.makeperson, name='makeperson'),
    path('legal_people/', views.getLegalPeople, name='legal_people'),
    path('pets/<str:name>/', views.getPetsOfPerson, name='pets_of_person'),
]