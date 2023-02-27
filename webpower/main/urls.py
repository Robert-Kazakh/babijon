from django.urls import path
from . import views

urlpatterns = [
    path('',views.calculation),
    path('base',views.base)
]
