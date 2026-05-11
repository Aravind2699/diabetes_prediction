from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('history/', views.history_view, name='history'),
    path('about/', views.about_view, name='about'),
    path('analytics/', views.analytics_view, name='analytics'),
]
