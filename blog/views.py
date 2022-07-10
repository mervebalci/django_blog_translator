# A view is basically could be either Python function or a Python class,
# which is an organizer or a middleman between the model of that particular webpage and the HTML code or also referred to as a template.
# So a view is the middleman that makes the communication between the MODEL and the HTML TEMPLATE.
# Because the model is just a database table and to bring/serve those data to a browser, HTML code is needed.

# View gets data form Model and gives those data to the HTML template.

from django.shortcuts import render
from .models import Post

# Create your views here.

class BlogView:
    model = Post
    template_name = 'blog.html'

# Django expects from this BlogView class to have a model and template_name variables.
# This model variable should point to the name of the model that should be connected to the blog.
# The model is Post which is class name from models.py and should be imported (line9).