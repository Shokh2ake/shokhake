from django.urls import path

from apps.views import RegisterFromView

urlpatterns = [
    path('register', RegisterFromView.as_view(), name='register_page')
]


