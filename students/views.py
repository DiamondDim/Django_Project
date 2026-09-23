from django.shortcuts import render
from django.http import HttpResponse


def example_view(request):
    return render(request, template_name='app/example.html')


def show_data(request):
    if request.method == 'GET':
        return render(request, template_name='app/show_data.html')


def submit_data(request):
    if request.method == 'POST':
        return HttpResponse("Данные отправлены")


def show_item(request, item_id):
    return render(request, template_name='app/item.html', context={'item_id': item_id})


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'students/contact.html')