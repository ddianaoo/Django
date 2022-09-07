from django import template
from news.models import *
from django.db.models import *

register = template.Library()

# @register.simple_tag(name='list_categories')
# def get_categories():
#     return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    #categories = Category.objects.all()
    #categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    context = {
        "categories": categories,
    }
    return context