from django.urls import path
from .views import *

urlpatterns = [
    path('', url_shortner, name='url_shortner'),
    path('<str:short_url>/', redirect_to_original, name='redirect_to_original'),
]