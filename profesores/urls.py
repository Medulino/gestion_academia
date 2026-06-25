from django.urls import path
from .views import (
    dashboard_profesor
)
urlpatterns = [
    path(
        'dashboard/',
        dashboard_profesor,
        name='dashboard_profesor'
    ),
]