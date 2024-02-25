from django.urls import path
from.import views

urlpatterns = [
    path('hello/', views.helloworld, name='helloworld'),
    path('banana/', views.banana, name='banana'),
    path('abra/', views.abra, name='abra'),
]