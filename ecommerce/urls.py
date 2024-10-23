from tempfile import template

from django.urls import path
from ecommerce.homepage.views import hello_geeks
from ecommerce.page2 import views

urlpatterns = [
    # path('', hello_geeks, name='homepage'),
    path('',template.html,name='home'),
    path('SignUp/',template/accounts/page2.html,name='signup'),
]

