from django.views.generic import FormView

from apps.forms import RegisterForm


class RegisterFromView(FormView):
    form_class = RegisterForm
    success_url = '/'

