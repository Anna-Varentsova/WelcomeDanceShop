from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination

from articles.permissions import IsAdminOrReadOnly
from goods.models import Goods
from goods.api.serializers import GoodSerializer

'''Если добавить authentication_classes = (TokenAuthentication, ),
# то можно настроить доступ к классу только по токену'''


# Класс для пагинации при просмотре api-data
class GoodsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 50


# Класс для отображения списка товаров по api.
# Просматривать список могут все, но можно убрать permission_classes,
# тогда смогут только авторизованные, т.к. см. WelcomedanceShop/settings/DEFAULT_PERMISSION_CLASSES
class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodSerializer
    pagination_class = GoodsAPIListPagination
    permission_classes = (IsAdminOrReadOnly,)

    # Метод для отображения выборки товаров
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Goods.objects.all()

        return Goods.objects.all().filter(pk=pk)



