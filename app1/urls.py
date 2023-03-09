from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('Siri/',Siri,name='Siri'),
    path('srujana/',srujana,name='srujana'),
]