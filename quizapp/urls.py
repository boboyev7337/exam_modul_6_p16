from django.contrib.admin import register
from django.contrib.auth import login
from django.urls import path, include

from .views import question, qiuz, result_list, sign_up

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', question, name='quistion'),
    path('results/', result_list, name='results'),
    path('sign_up/', sign_up, name='sign_up'),
]