from django.conf.urls import url
from django.contrib.auth import login, logout
from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import logoutview

urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),

    path('login/', LoginView.as_view(), name="login_url"),
    #path('login/', login, {'template_name': 'registration/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'registration/logout.html'}, name='logout'),
    path('register/', views.registerView, name="register_url"),
    #path('logout/', LogoutView.as_view(), name="logout"),
    path('requester/', views.requesterView, name='requester_url'),
    path('profile/', views.profile, name='profile')
    # path(
    #     'login/',
    #     LoginView.as_view(
    #         template_name="login.html",
    #         authentication_form=UserLoginForm
    #         ),
    #     name='login'
    # ),
]
