from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('saidas/', views.saidas, name='saidas'),
    path('entradas/', views.entradas, name='entradas'),
    path('notas/', views.notas, name='notas'),
    path('', views.paginainicial, name='paginainicial'),
     path('logout/', views.logout, name='logout'),
    
]
