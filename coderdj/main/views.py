from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home_view(request):
    return HttpResponse("<h1>Welcome to Home Page</h1><p>Главная страница.</p>")

def redirect_to_data(request):
    return HttpResponseRedirect(reverse('data'))

def data_view(request):
    return HttpResponse("<h1>Data Page</h1><p>Страница с данными.</p>")

def test_view(request):
    return HttpResponse("<h1>Test Page</h1><p>Тестовая страница.</p>")
