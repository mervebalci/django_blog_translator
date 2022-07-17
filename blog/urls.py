# After created the BlogView in views.py, some dummy data was created in DB Browser for SQLite.
# Those data includes title, content, date_created, slug, author and status which are in models.py
# Now, let's connect that slug and to do that: IMPORTING the VIEWS MODULE

from . import views
# . means current location and views is a file but when you import things, it becomes a module
from django.urls import path
# urls is another module of Django and path is a function

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('', views.HomeView.as_view(), name='home_view')
]
# When the user visits a certain URL, let's say example.com/dogs
# Django will go to DB table and search in each row for dogs.
# And when it finds the row has dogs, it will execute BlogView as view.


# After created index.html, how can user get this html template? What do they do?
# They enter a url in their browser. And to make that connection between html and url, a new path will be created (line12)
# Inside of this new path, HomeView is created as another view and this should be added in views.py as a new class.
# WHEN USER VISITS THIS '' URL, THIS HOMEVIEW WILL CALL THAT INDEX.HTML TEMPLATE TO BE RENDERED IN THE USER'S BROWSER


# There is another urls.py file inside my_site folder which contains the configurations of the Django project, not the Django apps.