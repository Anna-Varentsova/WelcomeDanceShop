from django.db import models
from django.urls import reverse


class Rubric(models.Model):
    name = models.CharField(verbose_name='Название',max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="rubric_URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'rubric_slug': self.slug})

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = 'рубрики'


class Gender(models.Model):
    gender = models.CharField(verbose_name='Пол', max_length=255, db_index=True)

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name_plural = "Пол"
        verbose_name = 'пол'


class Goods(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=255)
    content = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='WelcomeDanceShop photos/goods', blank=True)
    size = models.PositiveSmallIntegerField(verbose_name='Размер')
    label = models.CharField(verbose_name='Фирма', max_length=150)
    price = models.PositiveSmallIntegerField(verbose_name='Цена', )
    color = models.CharField(verbose_name='Цвет', max_length=100)
    category = models.CharField(verbose_name='Предназначено', max_length=255)
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True, verbose_name='Рубрика')
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True, verbose_name='Пол')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    quantity = models.PositiveSmallIntegerField(default=10, verbose_name='Количество')
    available = models.BooleanField(default=True, verbose_name='В наличии')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good', kwargs={'good_slug': self.slug})
    '''возможно, выше надо заменить args на args=[self.slug]'''

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = 'товары'
        ordering = ['-rubric']



