from django.shortcuts import render, redirect
from api.views import apiView

def rodada(request):
    if request.GET.get('buscarRodada') is not None:
        return redirect("rodada/"+request.GET.get('buscarRodada'))
    
    return render(request, "rodada.html")

def rodadaBuscada(request, rodadaBuscada=None):
    if rodadaBuscada is not None:
        original_get = request.GET
        request.GET = original_get.copy()
        request.GET['rodada'] = rodadaBuscada
        response = apiView.get_jogos(request)
    
    return render(request, "rodada.html", {'rodadaBuscada': rodadaBuscada, 'jogos': response.data})

def atualizarJogo(request, pk, rodadaBuscada=None):
    if rodadaBuscada is not None:
        original_get = request.POST
        request.PUT = original_get.copy()
        request.method = "PUT"
        apiView.update_jogo(request, pk)
        request.GET = original_get.copy()
        request.method = "GET"
        response = apiView.get_jogos(request)
        return render(request, "rodada.html", {'rodadaBuscada': rodadaBuscada, 'jogos': response.data})
    
    return render(request, "rodada.html")

