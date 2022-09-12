from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', GetNews.as_view(), name='get_news'),
    path('news/add-news/', AddNews.as_view(), name='add_news'),
    path('test/', test, name='test'),
    path('regist/', regist, name='regist'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
]