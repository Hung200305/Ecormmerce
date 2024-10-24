from django.contrib.messages.context_processors import messages
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from accounts.forms import *


def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user.refresh_from_db()  # load the profile instance created by the signal
    #         user.email = form.cleaned_data.get('email')
    #         user.password = form.cleaned_data.get('password')
    #         user.save()
    #         # raw_password = form.cleaned_data.get('password')
    #         # user = authenticate(username=user.username, password=raw_password)
    #         # login(request, user)
    #         return messages("Your account has been created!")
    # else:
    #     form = SignUpForm()
    # return render(request, 'accounts/signup.html', {'form': form})

    # return render(request, 'pages/homepage/template.html', {'form': form})
    if(request.POST):
        login_data = request.POST.dict()
        user = login_data.save()
        user.refresh_from_db()
        user.email = login_data.cleaned_data.get('email')
        user.password = login_data.cleaned_data.get('password')
        user.save()
        return messages("Your account has been created!")
# def detail_profile(request):
#     return render(request, 'accounts/detail_profile.html')
