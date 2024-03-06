from django.urls import path
from django.views.generic import CreateView
from . views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
