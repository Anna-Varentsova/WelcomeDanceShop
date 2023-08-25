from django.urls import path
from .views import GoodsIndex, ShowRubrics, show_good
urlpatterns = [
    path('', GoodsIndex.as_view(), name='goods'),
    path('<slug:good_slug>/', show_good, name='good'),
    path('category/<slug:rubric_slug>/', ShowRubrics.as_view(), name='rubric'),
]