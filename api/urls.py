from django.urls import path, include
from .views import get_view
urlpatterns = [
    path('<slug>/',get_view)
]
