from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('entity/', views.entity_list, name='entity_list'),
    path('entity/<int:id>/', views.entity_profile, name='entity_profile'),
    path('entity/add/', views.create_entity, name='create_entity'),
    path('entity/delete/<int:id>/', views.delete_entity, name='delete_entity'),
]
