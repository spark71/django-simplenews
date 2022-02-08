from django import forms
from django.core.exceptions import ValidationError
from .models import News
import re

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}), help_text='Максимум 150 символов')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# пример формы, не связанной с моделью

# class NewsForm(forms.Form):
#     # в параметре attrs - лежит класс для btsr
#     title = forms.CharField(max_length=150, label='Название:', widget=forms.TextInput(attrs={"class":"form-control"}))
#     # required - требует обязательного заполнения
#     content = forms.CharField(label='Текст: ', required=False, widget=forms.Textarea(attrs={"class":"form-control",
#                                                                                             "rows":5}))
#     #initial автоматические активирует чекбокс
#     is_published = forms.BooleanField(label='Опубликовано?', initial=True)
#     category = forms.ModelChoiceField(label='Категория:', queryset=Category.objects.all(), empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={"class":"form-control"}))
#

#Пример формы, связанной с моделью
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # Добавляет в шаблон все поля формы
        # fields = '__all__'
        # либо перечисляем в ручную
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        # проверка на содержание цифр
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title














