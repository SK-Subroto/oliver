from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('scoreboard/', views.scoreboard, name="scoreboard"),
    path('schedule/', views.schedule, name="schedule"),
    path('player/', views.playerProfile, name="player"),
    path('api/data/<str:id>', views.readFtp, name="data"),
    path('team/', views.team, name="team"),
    path('standing/', views.teamStanding, name="standing"),
]
