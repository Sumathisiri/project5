from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('abc/',abc,name='abc'),
    path('suresh/',suresh,name='suresh'),
    path('sumathi/',sumathi,name='sumathi'),
]