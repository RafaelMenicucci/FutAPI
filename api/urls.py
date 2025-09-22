from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.apiView import get_jogos, post_jogo, update_jogo

urlpatterns = [
    path("jogos/", get_jogos, name="get_jogos"),
    path("criar/jogo/", post_jogo, name="post_jogo"),
    path("atualizar/jogo/<int:pk>/", update_jogo, name="update_jogo"),
] + static(settings.STATIC_URL)
