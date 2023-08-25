from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.utils import DataMixin
from main.forms import RegistrationForm, EmailPostForm


# Главная страница
def index(request):
    context = {'title': 'Купить одежду, обувь, аксессуары для балета'}
    return render(request, 'main/index.html', context=context)


# Страница регистрации пользователя
class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'main/register.html'
    success_url = 'to_main'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('goods')


# Страница залогинивания пользователя
class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('goods')


# Функция разлогинивания
def logout_user(request):
    logout(request)
    return redirect('main:to_main')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>oops... there is no page:(<h1>')


# Страница обратной связи
def send(request):
    form = EmailPostForm
    return render(request, 'main/contacts.html', {'form': form})


# Обработчик формы обратной связи. Вместо your@mail.ru письма отправляются в консоль,
# т.к. см. WelcomeDanceShop/settings.py/EMAIL_BACKEND
def process_mail(request):
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Тема: {cd['name']}"
            message = f"{cd['comments']}"
            send_mail(subject, message, f'{cd["email"]}', ['your@mail.ru'], fail_silently=False)
            sent = True
    else:
        form = EmailPostForm()
    return redirect('main:success_mail')


# Страница успешной отправки письма обратной связи
def success_mail(request):
    return render(request, 'main/success_mail.html', {'title': 'Письмо отправлено'})

