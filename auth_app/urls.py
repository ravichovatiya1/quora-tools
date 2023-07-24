from django.urls import path
from . import views

# app name
app_name = "auth_app"


auth_patterns = [
    path('sign-up/', views.SignUpView.as_view(), name="sign_up"),
    path('sign-in/',views.SignInView.as_view(),name="sign_in"),
    path('logout/',views.LogOutView.as_view(),name="logout"),
]


