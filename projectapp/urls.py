from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('form', views.register, name='register'),
    #path('formpage', views.formpage, name='formpage'),

]
