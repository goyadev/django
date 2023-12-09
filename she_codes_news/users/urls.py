from django.urls import path
from .views import CreateAccountView
from .views import UserProfile

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # try to create a profile page 3 December: 
    path('user-profile/', CreateAccountView.as_view(), name='userProfile'),
]