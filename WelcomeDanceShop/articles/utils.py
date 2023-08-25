from articles.models import Articles


# необязательный миксин, сделан для практики
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        arts = Articles.objects.all()
        context['art_list'] = arts
        return context
