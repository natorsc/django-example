from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path(route='profile/', view=views.profile, name='profile'),
    path(route='signup/', view=views.SignUpView.as_view(), name='signup'),
]
