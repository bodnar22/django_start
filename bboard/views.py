from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'bboard/index.html', data)

def about(request):
    return render(request, 'bboard/about.html')
