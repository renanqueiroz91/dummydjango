
from django.urls import path
from . import views

app_name = "dummy"

urlpatterns = [
    path('', views.dummy, name='lead-list'),
    ]