from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('donor', views.donor, name='donor'),
    path('add_donor',views.add_donor, name="add_donor"),
    path('find_donor', views.find_donor, name ='find_donor'),
]