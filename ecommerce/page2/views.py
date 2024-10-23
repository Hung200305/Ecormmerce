from pyexpat.errors import messages

from django.shortcuts import redirect, render

from account.models import User


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