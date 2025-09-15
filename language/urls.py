from django.urls import path
from .views import home, change_language

urlpatterns = [
    path('', home),
    path('change-language/', change_language, name='change_language'),
]