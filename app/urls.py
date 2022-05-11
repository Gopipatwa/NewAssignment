from django.urls import path
from app import views


urlpatterns = [
    path('', views.FileView.as_view(),name="home"),
]
