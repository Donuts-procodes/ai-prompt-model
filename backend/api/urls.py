from django.urls import path
from .views import generate_prompt_image

urlpatterns = [
    path('generate/', generate_prompt_image),
]
