from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_star, name='view_star'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('stars/', views.StarList.as_view()),
    path('stars/<int:pk>/', views.StartDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
