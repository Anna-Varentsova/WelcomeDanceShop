from django.conf.urls.static import static
from django.urls import path


from WelcomeDanceShop import settings
from .views import show_art, AllArticles, AddArt

urlpatterns = [
    path('<slug:art_slug>/', show_art, name='art'),
    path('add_art/add_art/', AddArt.as_view(), name='add_art'),
    path('', AllArticles.as_view(), name='to_articles'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)