# A webpage contains 3 components: a model, a view and an HTML template.
# And MODEL contains the database fields of the web page!!!
# With other words, MODEL keeps the code of the communication with database.

from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Creating a STATUS variable
STATUS = ((0, 'Draft'), (1, 'Publish'))
# 0 stands for Draft and 1 stands for Publish
# The admin(content creator) will see either draft or publish in that dropdown list.


# Creating a class to represent a blog post:
class Post(models.Model):
# Post is not a simple class, it should be a class which inherits from models.Model
# So Model is a specific class, which is designed by the Django authors (the developers of Django.
# And it's designed to contain fields of data.
    title = models.CharField(max_length=200)
    # When the content creator creates a TITLE, that title will be stored in the title fields of the Post table.
    # So there will be a text box that will allow up to 200 characters for the title of the blog.
    content = models.TextField()
    # Content is the body of the blog.
    date_created = models.DateTimeField(auto_now_add=True)
    # When the content creator will be creating a new blog post from the admin interface, ...
    # So they will be writing a title, a content.
    # And then there will be a save button there where they can press that save button. 
    # And the posts will be live.
    # When the content creator presses that button, this class will be instantiated and it will generate the current date and time.
    # And that current date and time will be injected into the date created field of the post table in the db.sqlite3 database.
    slug = models.SlugField(max_length=200, unique=True)
    # SLUG will be recording the part of the URL after the domain.
    # Let's say the domain is example.com and the blog is about dogs.
    # Then the slug will be "/dogs". The complete URL would be "example.com/dogs"
    # The user(content creator) will enter the slug in the admin interface.
    # unique=True means if the admin(the content creator) enters a slug, which has been answered before, 
    # that would not allow the new slug to be created because there can't be two pages with the same URL.
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # to and on_delete values will be get from another database table, which has been created by Django already (line7).
    # ForeignKey field type means that the value of these database fields will come from another database table. 
    # In this case is the User's database table.
    # And this field will create on the admin interface a dropdown list where the the content creator can choose between different usernames.
    # "on_delete=models.CASCADE" means that if a user is deleted from the user database table, the user posts will also be deleted.
    # This is what CASCADE does.
    status = models.IntegerField(choices=STATUS, default=0)
    # On the admin interface, there will be a status dropdown list which will contain two options, draft and publish.
    # The content creator could choose to save that article either as draft or as published. 
    # This would make it easier for content creators to organize blogs because they could save an article as a draft.
    # And then in Django app, they could make a conditional not to publish such articles that have a status as draft, 
    # but only publish those who have a status as published.
    # So this would be a good way to distinguish between the two types of posts, articles.


# To Apply the Model to the Database
# Inside terminal in the virtual environment;
# > python manage.py makemigrations
# > python manage.py migrate
# Then refresh it in DB Browser, you'll see blog_post table has been added.