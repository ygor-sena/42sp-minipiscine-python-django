from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("ex00/", HomePageView.as_view(), name="index.html"),
]