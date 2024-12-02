from ride.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('auto/',auto,name='auto'),
]