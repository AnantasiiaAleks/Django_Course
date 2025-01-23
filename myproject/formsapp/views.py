import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserFormSimple, ManyFieldsForm, ManyFieldsFormWidget, Userform, ImageForm
from .models import User

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserFormSimple(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserFormSimple()
    return render(request, 'formsapp/userform.html', {'form': form})


# def many_fields_form(request):
#     if request.method == 'POST':
#         form = ManyFieldsForm(request.POST)
#         if form.is_valid():
#             # Какая-то обработка данных из формы
#             logger.info(f'Получили данные {form.cleaned_data=}.')
#     else:
#         form = ManyFieldsForm()
#     return render(request, 'formsapp/many_fields_form.html', {'form': form})

def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Какая-то обработка данных из формы
            logger.info(f'Получили данные {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'formsapp/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранен'
    else:
        form = Userform()
        message = 'Заполните форму'
    return render(request, 'formsapp/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'formsapp/upload_image.html', {'form': form})
