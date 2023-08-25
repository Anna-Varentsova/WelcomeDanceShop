from django.urls import path
from .views import ArticlesAPIList, ArticlesAPIUpdate, ArticlesAPIDestroy

app_name = 'api_art'

urlpatterns = [
    path('articles/', ArticlesAPIList.as_view()),
    path('articles_update/<int:pk>/', ArticlesAPIUpdate.as_view()),
    path('articles_destroy/<int:pk>/', ArticlesAPIDestroy.as_view()),
]
