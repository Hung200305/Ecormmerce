# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse

from ecommerce.page2.views import render_account


# from .models import *
# from cart.models import Cart
# from accounts.models import Profile


# Create your views here.


def render_homepage(request):
    context = {
        'signUp': render_account
    }
    return render(request, 'pages/homepage/template.html', context)
