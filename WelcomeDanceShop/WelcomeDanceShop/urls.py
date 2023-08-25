from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from WelcomeDanceShop import settings
from main.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),

    path('welcome-dance-shop/api/', include('goods.api.urls', namespace='api')),
    path('welcome-dance-shop/api_art/', include('articles.api.urls', namespace='api_art')),    # работа с api статей
    path('welcome-dance-shop/api_art/articles_auth/', include('rest_framework.urls')),    # авторизация по сессии

    path('api/v1/auth/', include('djoser.urls')),    # авторизация по токенам - список юзеров(добавить /users)
    re_path(r'^auth/', include('djoser.urls.authtoken')),    # авторизация по токенам (добавить /auth + login/logout)

    path('welcome-dance-shop/cart/', include('cart.urls', namespace='cart')),
    path('welcome-dance-shop/orders/', include('orders.urls', namespace='orders')),
    path('welcome-dance-shop/payment/', include('payment.urls', namespace='payment')),
    path('welcome-dance-shop/articles/', include('articles.urls'), name='to_articles'),
    path('welcome-dance-shop/goods/', include('goods.urls'), name='goods'),
    path('', include('main.urls', namespace='main')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
