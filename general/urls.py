from django.urls import path

from .views import Map

urlpatterns = [
    path('map/', Map.as_view()),
]
