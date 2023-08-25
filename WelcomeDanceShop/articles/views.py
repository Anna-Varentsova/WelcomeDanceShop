from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from articles.forms import AddArtForm
from articles.models import Articles
from articles.utils import DataMixin


class AllArticles(DataMixin, ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = 'art_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Статьи')
        return {**context, **c_def}


def show_art(request, art_slug):
    artic = get_object_or_404(Articles, slug=art_slug)
    context = {'artic': artic,
               'title': artic.title}
    return render(request, 'articles/art.html', context=context)


# Разрешение необходимо, чтобы неразрешенные пользователи не могли добавить статью, просто пройдя по прямой ссылке
# Неавторизованный пользователь при использовании прямой ссылки получит 404 PageNotFound;
# авторизованный, но без разрешения - 403 Forbidden.
# При добавлении статьи поле user у нее будет NULL (см. модель Articles)
class AddArt(PermissionRequiredMixin, CreateView):
    permission_required = 'articles.add_articles'
    model = Articles
    form_class = AddArtForm
    template_name = 'articles/add_art.html'
    context_object_name = 'form'
    extra_context = {'title': 'Добавить статью'}
    success_url = reverse_lazy('to_articles')

