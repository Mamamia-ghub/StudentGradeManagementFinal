from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]