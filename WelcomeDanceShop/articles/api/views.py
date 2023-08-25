
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from articles.models import Articles
from articles.api.serializers import ArticlesSerializer
from articles.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

'''Если добавить authentication_classes = (TokenAuthentication, ),
# то можно настроить доступ к классу только по токену'''


# просматривать список могут все, но можно убрать permission_classes,
# тогда смогут только авторизованные,
# т.к. см. WelcomedanceShop/settings/DEFAULT_PERMISSION_CLASSES
class ArticlesAPIList(ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAdminOrReadOnly, )


# изменять статью может только ее автор(по умолчанию у всех стоит админ)
class ArticlesAPIUpdate(RetrieveUpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# удалять статью могут только админы (is_staff)
class ArticlesAPIDestroy(RetrieveDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAdminOrReadOnly, )
