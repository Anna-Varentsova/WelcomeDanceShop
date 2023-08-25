from goods.models import Rubric


# Миксин для постоянного отображения вверху каталога списка категорий
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Rubric.objects.all()
        context['cats'] = cats
        return context

