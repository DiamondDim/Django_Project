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