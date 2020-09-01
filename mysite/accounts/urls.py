from django.conf.urls import url

from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from .views import logoutview, SignUpView
#app_name = 'accounts'
urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('register/', SignUpView.as_view(), name='register_url'),
    path('login/', views.loginview, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/requester/', views.requesterView, name='requester_url'),
    path('requester/', views.requesterView, name='requester_url'),
    path('<int:pk>/profile/', views.ViewProfile.as_view(), name='view_profile'),
    path('requesterupdate/', views.edit_profile, name='requester_update'),
    path('recipient/', views.recipientView, name='recipient'),
    path('password/', views.edit_password, name="password")
    #path('requesterupdate/', views.RequesterUpdate.as_view(), name='requesterupdate'),
    # path('register/', views.registerView, name="register_url"),
    #path('<int:pk>/requesterupdate', views.RequesterUpdate.as_view(), name='requesterupdate'),
    #path('profile/edit/', views.edit_profile, 'edit_profile')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path(
    #     'login/',
    #     LoginView.as_view(
    #         template_name="login.html",
    #         authentication_form=UserLoginForm
    #         ),
    #     name='login'
    # ),
]
