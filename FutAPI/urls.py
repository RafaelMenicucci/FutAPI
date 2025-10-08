from django.contrib import admin
from django.urls import path, include
from .views import signin, rodada


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', signin.signin, name="signin"),
    path('signin', signin.signin, name="signin"),
    path('staff/rodada', rodada.rodada, name="rodada"),
    path('staff/rodada/<int:rodadaBuscada>/', rodada.rodadaBuscada, name='rodadaBuscada'),
    path("staff/atualizar/jogo/<int:pk>/<int:rodadaBuscada>/", rodada.atualizarJogo, name="atualizarJogo"),
]
