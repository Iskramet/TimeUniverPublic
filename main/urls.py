from django.urls import path
from django.contrib.auth import views as as_view

from . import views

urlpatterns = [
    path('', views.promo),
    path('login/', as_view.LoginView.as_view(), name='login'),
    path('<group>/', views.shedule_view, name = 'group'),
    path('<group>/<int:pk>/', views.lesson, name='lesson'),
    path('<group>/day_week/<int:pk>/', views.day_week, name='day_week'),
    path('<group>/<int:lesson>/delete', views.remove_lesson, name='remove_lesson')
]