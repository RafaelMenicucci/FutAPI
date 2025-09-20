from django.urls import path
from .views.apiView import get_jogos, post_jogos

urlpatterns = [
    path('jogos/', get_jogos, name='get_jogos'),
    path('criar/jogo/', post_jogos, name='post_jogos'),
]