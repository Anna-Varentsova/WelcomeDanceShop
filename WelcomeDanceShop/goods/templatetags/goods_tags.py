from django import template
from goods.models import Rubric

register = template.Library()


# Пользовательский шаблон (для практики)
@register.simple_tag()
def show_categories():
    return Rubric.objects.all()