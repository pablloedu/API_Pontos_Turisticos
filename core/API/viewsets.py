from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']
    serializer_class = PontoTuristicoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = PontoTuristico.objects.filter(nome=nome)
        if descricao:
            queryset = PontoTuristico.objects.filter(descricao=descricao)

        return queryset