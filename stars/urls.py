from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_star, name='view_star'),
    path('add/', views.add, name='add'),
]
