from django.urls import path
from farmsetu_app import views

urlpatterns = [
    path("", views.WeatherView.as_view(),name="home"),
]
