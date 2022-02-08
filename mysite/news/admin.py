from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget

from .models import News, Category
# Register your models here.





class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title','category','created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    # Чекбокс для публикации
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    # Поле для поиска в админке по полям: title и content
    search_fields = ('title', 'content')
    fields = ('title','category', 'content','photo' ,'get_photo', 'is_published', 'created_at', 'views','updated_at')
    readonly_fields = ('get_photo','created_at','updated_at', 'views')
    # Добавляет панель для сохранения на верх
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'No photo'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    # Оставляем запятую, чтобы сохранить структуру кортежа
    search_fields = ('title',)





#Именно такой порядок регистрации, он важен
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'


