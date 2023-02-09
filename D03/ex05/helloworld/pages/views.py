# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "helloworld.html"


class HelloWorldPageView(TemplateView):  # new
    template_name = "helloworld.html"
