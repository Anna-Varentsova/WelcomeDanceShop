from django.conf.urls.static import static
from django.urls import path
from WelcomeDanceShop import settings
from cart.views import cart_detail, cart_add, cart_remove

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('', cart_detail, name='cart_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)