from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.jogos import Jogos
from ..serializers.jogosSerializer import JogosSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_jogos(request):
    print(request.user.is_staff)
    jogos = Jogos.objects.all()
    serializer = JogosSerializer(jogos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def post_jogos(request):
    serializer = JogosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
        