# DEFINE IMPORTS
from django.urls import path
from . import views

# DEFINE APP NAME: 'eskak'
app_name = 'eskak'

# URL Paths Resolved within the list: 'urlpatterns'
urlpatterns = [
    path('', views.landing_view, name='landing_view'),
    path('new-entry/', views.new_entry_view, name='new_entry_view'),
    path('create-entry/', views.new_entry_create, name='new_entry_create'),
    path('previous-entries/', views.previous_entry_view, name='previous_entry_view'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]

'''
Made with ❤️
------------
BRANDEN VAN STADEN -
    All rights reserved | September 2023
-------------------------------------
'''