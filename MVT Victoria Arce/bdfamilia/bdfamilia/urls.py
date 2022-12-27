from django.contrib import admin
from django.urls import path

from family.views import create_relative, list_relatives

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create-relative/', create_relative, name = 'create_relative'),
    path('list-relatives/', list_relatives, name = 'list_relatives'),
    
]
