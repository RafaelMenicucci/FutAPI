from rest_framework import serializers
from ..models.jogos import Jogos


class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogos
        fields = "__all__"
