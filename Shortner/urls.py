from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.Home,name='Home'),
    path('linkgen',views.link_gen,name='Home'),
    path('<str:link>', views.navigator, name='navigator'),

]
