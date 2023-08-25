from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тема ")
    content = models.TextField(blank=True, verbose_name="Текст")
    content2 = models.TextField(blank=True, verbose_name="Текст")
    content3 = models.TextField(blank=True, verbose_name="Текст")
    content4 = models.TextField(blank=True, verbose_name="Текст")
    photo = models.ImageField(upload_to='WelcomeDanceShop photos/articles', verbose_name="Фото")
    photo1 = models.ImageField(upload_to='WelcomeDanceShop photos/articles', verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    # метод для создания URL статьи по ее слагу
    def get_absolute_url(self):
        return reverse("art", kwargs={'art_slug': self.slug})

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name = "статьи"

