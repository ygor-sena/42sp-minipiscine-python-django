# pages/urls.py
from django.urls import path
from .views import HomePageView, HelloWorldPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="helloworld"),
    path("helloworld/", HelloWorldPageView.as_view(), name="helloworld"),
]