from django.shortcuts import render, redirect
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .utils import MyMixin

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.contrib.auth import login, logout
from django.contrib import messages



def regist(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #только регистрация
            form.save()
            messages.success(request, 'Успешная регистрация')
            return redirect('signin')

            #регистрация и вход
            #user = form.save()
            #login(request, user)
            #messages.success(request, 'Успешная регистрация')
            #return redirect('home')

        else:
            messages.error(request, "Хуйня переделывай")
    else:
        form = UserRegisterForm()
    return render(request, 'news/regist.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/signin.html', {'form': form})



def signout(request):
    logout(request)
    return redirect('home')



class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Список новостей'}
    mixin_prop = 'hello пидорасик'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.select_related('category').filter(is_published=True)


class NewsByCategory(MyMixin, ListView):
    model = News
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 4

    def get_queryset(self):
        return News.objects.select_related('category').filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context


class GetNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'


class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    # raise_exception = True
    login_url = '/admin/'


# def test(request):
#     objects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r']
#     paginator = Paginator(objects, 3)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     context = {
#         'page_obj': page_objects
#     }
#     return render(request, 'news/test.html', context)

