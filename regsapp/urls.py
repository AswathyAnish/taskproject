from django.urls import path

from . import views
#app_name='regsapp'

urlpatterns = [
    path('form', views.register, name='register'),
    path('login', views.login, name='login'),
    path('newpage', views.newpage, name='newpage'),
    path('formpage', views.formpage, name='formpage'),

    #path('logout', views.logout, name='logout'),

]
