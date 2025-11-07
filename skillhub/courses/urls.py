from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<str:course_slug>/', views.course, name='course'),
    path('category/<slug:category_slug>/', views.category, name='category'),
]