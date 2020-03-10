from django.urls import path
from . import views

urlpatterns = [
    path('email_list_signup/', views.email_list_signup, name='email_list_signup'),
]