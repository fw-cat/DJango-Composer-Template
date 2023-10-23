from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='top'),
    path('result', views.result, name='top'),
]
