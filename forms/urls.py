from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_forms, name="all_forms"),

]
