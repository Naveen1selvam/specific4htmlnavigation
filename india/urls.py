from django.urls import path
from india.views import *
app_name='india'
urlpatterns=[
    path('bcci/',bcci,name='bcci'),
    path('ipl/',ipl,name='ipl'),
]