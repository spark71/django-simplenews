from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from  django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.core.paginator import Paginator

from .utils import MyMixin

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm

from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрированы')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form":form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form":form})


def user_logout(request):
    logout(request)
    return redirect('login')



def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8' ]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj':page_objects})

class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    extra_context = {'title':'Главная'}
    # mixin_prop = 'hello world'
    paginate_by = 3


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Идёт вызов методов из MyMixin
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')





# def index(request):
#     #print(dir(request))
#     news = News.objects.all()
#     #Для вывода категорий был создан тег в templatetags
#     # categories = Category.objects.all()
#
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#         # 'categories': categories,
#     }
#     return render(request, template_name='news/index.html', context=context)


    #res = '<h1>Список новостей</h1>'
    #for item in news:
    #    res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div><hr>'
    # В терминале - <WSGIRequest: GET '/news/'>
    #return HttpResponse(res)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home/home_news_list.html'
    context_object_name = 'news'
    # Запрещаем показ пустых маршрутов, они будут возвращать 404ю ошибку
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news':news, 'category':category})
#



# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item":news_item})


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'

#наследуемся от LoginRequiredMixin для ограничения добавления новостей
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

    # raise_exception = True
    # После создания новости вернёт редирект на главную страницу, а по умолчанию при создании
    # новости срабатывает метод get_absolute_url и перекидывает нас на страницу созданной новости (т.е её просмотр)
    # success_url = reverse_lazy('home')



# def add_news(request):
#     if request.method == 'POST':
#         # Получаем данные из формы, которые пришли с помощью метода POST
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # если данные прошли валидацию, то мы помещаем их в специальный словарь - **cleaned_data
#            # print(form.cleaned_data)
#            #  news = News.objects.create(**form.cleaned_data)
#            # на всякий случай смотреть 24-й урок
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {"form":form})
#













