from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from ..models.jogos import Jogos
from ..serializers.jogosSerializer import JogosSerializer
from ..enums.time import Time


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_jogos(self):
    jogos = Jogos.objects.all().order_by("rodada")
    serializer = JogosSerializer(jogos, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_rodada(request):
    rodadaId = request.query_params.get("rodada")
    if rodadaId is not None:
        jogos = Jogos.objects.filter(rodada=rodadaId).order_by("rodada")
        serializer = JogosSerializer(jogos, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def post_jogo(request):
    data = request.data
    try:
        int(data["time_casa"])
        time = "T" + data["time_casa"]
        data["time_casa"] = Time[time].value
    except ValueError:
        pass
    try:
        int(data["time_fora"])
        time = "T" + data["time_fora"]
        data["time_fora"] = Time[time].value
    except ValueError:
        pass
    serializer = JogosSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_jogo(request, pk):
    try:
        jogo = Jogos.objects.get(pk=pk)
    except Jogos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = request.data
    try:
        int(data["time_casa"])
        time = "T" + data["time_casa"]
        data["time_casa"] = Time[time].value
    except ValueError:
        pass
    try:
        int(data["time_fora"])
        time = "T" + data["time_fora"]
        data["time_fora"] = Time[time].value
    except ValueError:
        pass
    serializer = JogosSerializer(jogo, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
