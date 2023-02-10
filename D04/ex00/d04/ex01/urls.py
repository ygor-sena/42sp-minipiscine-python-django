# djangotemplates/example/urls.py

from django.conf.urls import url
from example import views

urlpatterns = [
    url("", views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url("about/", views.AboutPageView.as_view(), name='about'),
]
