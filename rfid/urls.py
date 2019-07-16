from . import views
from django.urls import path

app_name='rfid'


urlpatterns = [
    path('',views.assesment, name='index'),
]