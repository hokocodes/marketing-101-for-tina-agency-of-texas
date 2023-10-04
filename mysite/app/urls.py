from django.urls import path
from . import views
from app.views import index

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path('', index),
]

