from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.contact_list, name='contact_list'),
]