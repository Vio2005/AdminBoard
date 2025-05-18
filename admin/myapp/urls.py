from django.urls import path
from.views import *

urlpatterns=[
    path('home/',home,name='home'),
    path('sidebar/',home,name='sidebar'),
    path('icon/',home,name='icon'),
]