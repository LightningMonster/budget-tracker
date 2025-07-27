from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),  # Landing page
    path('signup/', views.signup_view, name='signup'),  # Sign up page
    path('login/', views.login_view, name='login'),  # Log in page
    # Add more paths here...
]
