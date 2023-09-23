# DEFINE IMPORTS
from django.urls import path
from . import views

# DEFINE APP NAME: 'users'
app_name = 'users'

# URL Paths Resolved within the list: 'urlpatterns'
urlpatterns = [
    # USER REGISTRATION ROUTES
    path('auth/', views.login_user, name='login_user'),
    path('login/', views.login_view, name='login_view'),
    # USER REGISTRATION ROUTES
    path('register/', views.register_view, name='register_view'),
    path('create/', views.register_user, name='create_user'),
    # USER MANAGEMENT ROUTES
    path('profile/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_view, name='logout_view'),

]