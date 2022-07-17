# A view is basically could be either Python function or a Python class,
# which is an organizer or a middleman between the model of that particular webpage and the HTML code or also referred to as a template.
# So a view is the middleman that makes the communication between the MODEL and the HTML TEMPLATE.
# Because the model is just a database table and to bring/serve those data to a browser, HTML code is needed.

# View gets data form Model and gives those data to the HTML template.

from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

# Django expects from this BlogView class to have a model and template_name variables.
# This model variable should point to the name of the model that should be connected to the blog.
# The model is Post which is class name from models.py and should be imported (line9).


class HomeView(generic.TemplateView):
    template_name = 'index.html'
    # TemplateView means when you only need to render a template without getting data from a model.
    # DetailView gets data from models and passes them to templates.
    # So, this class doesn't need a MODEL. Because index.html is a static page.
    # It's not getting any data from a database like blog.html
    # However, blog.html gets data from database such as title, content, author.