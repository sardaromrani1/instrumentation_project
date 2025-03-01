from django.urls import path
from . import views

urlpatterns=[
    path('add/', views.add_instrument, name='add_instrument'),
    path('list/', views.instrument_list, name='instrument_list'),
]