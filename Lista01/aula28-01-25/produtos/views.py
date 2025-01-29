from rest_framework.viewsets import ModelViewSet
from .models import Produto, Fornecedor
from .serializers import ProdutoSerializer, FornecedorSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

# Create your views here.
