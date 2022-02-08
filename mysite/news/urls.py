from django.urls import path
from .views import *



urlpatterns = [
    # Для news во views будет вызвана главная страничка
    # Третьим параметром задаём имя для маршрута name. Использование name удобно, когда необходимо менять имя маршртуа,
    # засчёт параметра можно поменять имя только в urls.py

    # path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('test/', test, name='test'),
    #Можем передать класс ListView в качестве view-ф-ии
    path('', HomeNews.as_view(), name='home'),
    # path('cat/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title':'Какой-то тайтл'}), name='category'),
    #маршрут для просмотра отдельной новости
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),


]








