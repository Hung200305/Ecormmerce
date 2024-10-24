from pyexpat.errors import messages

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username = email,password=password)
            login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect('templates/pages/template.html')
    else:
        form = UserCreationForm()

    return render(request, 'authentication',{'form':form},)

def create_user(request):
    if(request.method == 'POST'):
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        try:
            user = User.objects.create_user(email=email, password=password)
            user.save()
            messages.success(request, 'Your account has been created!')
            return redirect('templates/pages/template.html')

        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')

    return render(request,'templates/accounts/page2.html')

# def create_user(self, email, password=None):
#     if not email:
#         raise ValueError('The given email must be set')
#     email = self.normalize_email(email)
#     user = self.model(email=email)
    user.set_password(password)
    user.save(using=self._db)
    return user

def render_account(request):
    return render(request, 'pages/accounts/page2.html', {})