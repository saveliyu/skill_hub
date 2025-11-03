from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<str:course_slug>/', views.course, name='course'),
    path('category/<int:category_id>/', views.category, name='category'),
]