from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

# Роутер нужен для формирования  динамических URL после префикса goods
router = routers.DefaultRouter()
router.register(r'goods', views.GoodsViewSet, basename='goods')

urlpatterns = [
    path('', include(router.urls), name='goods_list'),
]
