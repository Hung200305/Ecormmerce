from django import forms

from accounts.models import User


# class SignUpForm():
#     email = forms.EmailField(label=("E-mail"), widget=forms.EmailInput, )
#     password = forms.CharField(widget=forms.PasswordInput,
#                                 label=("Password"))

class SignUpForm():
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password')
