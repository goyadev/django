from django.urls import path
from .views import CreateAccountView, UserProfile

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # try to create a profile page 3 December, 9 December: 
    path('user-profile/<int:pk>/', UserProfile.as_view(), name='userProfile'),
]