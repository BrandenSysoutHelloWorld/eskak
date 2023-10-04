from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls, name='admin'),
    path('users/', include('users.urls')),
    path('eskak/', include('eskak_app.urls'))
]
