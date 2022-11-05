from django import forms;
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # Password: <input type="password" value="FakePSW" id="myInput">
   # <input type = "checkbox" onclick = "myFunction()"> Show Password

    class Meta:
        model = User  # it is mysql-db model-table(for auth_app_db)

        fields = ['username', 'password', 'email', 'first_name', 'last_name'];
