from rest_framework import serializers
from core.models import PontoTuristico
from atracoes.API.serializers import AtracaoSerializer
from enderecos.API.serializers import EnderecoSerializer

class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'endereco', 'foto', 'atracoes', 'comentarios', 'avaliacoes',)

