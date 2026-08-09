from django.urls import path
from .views import classify_image

urlpatterns = [
    path('', classify_image, name='classify'),
    
]