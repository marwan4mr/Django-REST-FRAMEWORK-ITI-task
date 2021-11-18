from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views
app_name="account=v1"
urlpatterns = [
    path('get-token', obtain_auth_token),
    path('example', views.example_view),
    path('signup', views.sign_up),
    path('login', obtain_auth_token, name='login'),
    path('logout', views.logout, name="logout" )
]