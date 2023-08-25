from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from cart.forms import CartAddProductForm
from .forms import SearchGoodForm
from .models import Goods, Rubric
from .utils import DataMixin

'''Поиск товара в форме чувствителен к регистру (особенность SQLite)
   Поиск товара при ВЫБРАННОЙ ранее категории выдает только товары из ЭТОЙ категории'''

# Отображаем 1 товар
def show_good(request, good_slug):
    good = get_object_or_404(Goods, slug=good_slug)
    cart_product_form = CartAddProductForm()
    context = {'good': good, 'title': good.title, 'id': good.id, 'cart_product_form': cart_product_form}
    return render(request, 'goods/good.html', context=context)


# Отображаем список товаров и форму поиска
class GoodsIndex(DataMixin, ListView):
    model = Goods
    template_name = 'goods/index.html'
    context_object_name = 'g_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Каталог товаров', form=SearchGoodForm(self.request.GET))
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        filters = {}
        title = self.request.GET.get('title')
        gender = self.request.GET.get('gender')
        if title:
            filters['title__contains'] = title
        if gender:
            filters['gender'] = gender
        new_context = Goods.objects.filter(**filters).order_by('rubric')
        return new_context


# Отображаем список товаров и форму поиска при нажатии на категорию
class ShowRubrics(DataMixin, ListView):
    paginate_by = 4
    model = Goods
    template_name = 'goods/index.html'
    context_object_name = 'g_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товары по категориям', form=SearchGoodForm(self.request.GET))
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        filters = {}
        title = self.request.GET.get('title')
        gender = self.request.GET.get('gender')
        if title:
            filters['title__contains'] = title
        if gender:
            filters['gender'] = gender
        return Goods.objects.filter(rubric__slug=self.kwargs['rubric_slug'], **filters)

