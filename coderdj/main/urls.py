from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_data, name='home'),
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
]


