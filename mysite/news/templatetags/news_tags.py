from django import template
from news.models import *
from django.db.models import *
from django.core.cache import cache

register = template.Library()

# @register.simple_tag(name='list_categories')
# def get_categories():
#     return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #cache
    #categories = cache.get('categories') #try to get data from cache
    #if not categories:
    #    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #    cache.set('categories', categories, 30) #save the received data to cache
    #instead of this 4 lines you can use cache.get_or_set()

    return {"categories": categories}
