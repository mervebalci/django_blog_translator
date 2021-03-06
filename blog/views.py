# A view is basically could be either Python function or a Python class,
# which is an organizer or a middleman between the model of that particular webpage and the HTML code or also referred to as a template.
# So a view is the middleman that makes the communication between the MODEL and the HTML TEMPLATE.
# Because the model is just a database table and to bring/serve those data to a browser, HTML code is needed.

# View gets data form Model and gives those data to the HTML template.

from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.


# DetailView to render html templates that gets data from a model
class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'
# Django expects from this BlogView class to have a model and template_name variables.
# This model variable should point to the name of the model that should be connected to the blog.
# The model is Post which is class name from models.py and should be imported (line9).


# TemplateView to render html templates without data from a model
class AboutView(generic.TemplateView):
    template_name = 'about.html'
    # TemplateView means when you only need to render a template without getting data from a model.
    # DetailView gets data from models and passes them to templates.
    # So, this class doesn't need a MODEL. Because about.html is a static page.
    # It's not getting any data from a database like blog.html
    # However, blog.html gets data from database such as title, content, author.


# ListView is specialized in rendering multiple data rows/multiple posts
class PostList(generic.ListView):    # class name has to be in the same format with the one inside for loop in index.html
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'
    # This type of class expects a queryset variable which should be equal to Post.
    # Post is the model class in models.py
    # After that, query the objects and then add a filter. So, it will only show the posts that are published.
    # And to put them in an order maybe according to date created, use 'order_by'
    # With this version, webpage will always show the oldest post on the top and keeps adding the new ones at the end.
    # If you want to change it to show the newest one always on top, then you need to write like this .order_by('-date_created')
    
    # AFTER THE NEW VIEW IS CREATED, THE NEW PATH SHOULD BE ADDED IN URLS.PY