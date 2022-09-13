from django.urls import path
from .views import *

from django.views.decorators.cache import cache_page

urlpatterns = [
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', GetNews.as_view(), name='get_news'),
    path('news/add-news/', AddNews.as_view(), name='add_news'),

    path('contact/', contact, name='contact'),

    path('regist/', regist, name='regist'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
]