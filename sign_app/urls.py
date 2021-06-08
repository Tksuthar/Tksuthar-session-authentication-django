from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls import handler404, handler400

app_name = 'sign_app'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('color-track', views.color, name = 'color-track'),
    path('signin', views.signin, name = 'signin'),
    path('logout', views.log_out, name = 'logout'),
    path('signup', views.signup, name = 'signup'),
]

handler404 = 'sign_app.views.error_404'
