from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.apiView import get_jogos, post_jogos

urlpatterns = [
    path("jogos/", get_jogos, name="get_jogos"),
    path("criar/jogo/", post_jogos, name="post_jogos"),
] + static(settings.STATIC_URL)
