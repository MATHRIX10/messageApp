from django.shortcuts import render
from .models import Post
from django.views.generic import  TemplateView,ListView


class Index(ListView) : 
    model = Post
    template_name = 'pages/index.html'
