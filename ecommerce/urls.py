from tempfile import template

from django.urls import path, include
# from ecommerce.homepage.views import hello_geeks
from ecommerce.homepage import views
from ecommerce.page2.views import render_account

# from ecommerce.page2 import create_user

urlpatterns = [
    path('', views.render_homepage ,name='homepage'),
    path('sign-up',render_account,name='signup'),
    path('',include('django.contrib.auth.urls')),
]

