from django.urls import path, include
from .views import get_view, post_view
urlpatterns = [
    path('create',post_view),
    path('<slug>/',get_view),
]
