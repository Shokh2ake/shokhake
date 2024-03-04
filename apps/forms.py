from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import models, CharField, PasswordInput

from apps.models import User


class RegisterForm(models.ModelForm):
    confirm_password = CharField(max_length=255, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Password doesn't match")
        return make_password(password)
