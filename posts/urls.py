from django.urls import path
from posts.views import *

urlpatterns = [
   path('', hello_world, name = 'hello_world'),
   path('page', introduction, name='my-page'),
   ]