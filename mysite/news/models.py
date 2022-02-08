from django.db import models
from django.urls import reverse


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    # blank - данное поле не явл-ся обязательным к заполнению
    content = models.TextField(blank=True, verbose_name='Контент')
    # auto_now_add - при редактировании новости дата остаётся прежней
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    # auto_now - при каждом обновлении записи - оновляем соответсвующее поле
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # upload_to - адрес загрузки
    # сохранения фото в формате %Y %m %d - год месяц день, в проекте будет создана соотв. структура папок
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    # Jn
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    # on_delete - удаление связей
    category = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name='Категория')

    # кол-во просмотров. С каждым просмотром счётчик будет увеличиваться
    views = models.IntegerField(default=0)


    def get_absolute_url(self):
        #азвание маршрута и необходимый параметр для построения данного маршрута
        return reverse('view_news', kwargs={"pk": self.pk})

    # Строковое отображение titl'a в QuerySet
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        # Порядок сортировки по полю created_at
        ordering = ['-created_at']


# Создаём отдельный класс для категорий
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий')


    def get_absolute_url(self):
        #азвание маршрута и необходимый параметр для построения данного маршрута
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
