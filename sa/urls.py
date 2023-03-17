from django.urls import path
from sa.views import *
app_name='sa'
urlpatterns=[
    path('south/',south,name='south'),
    path('saca/',saca,name='saca'),

]