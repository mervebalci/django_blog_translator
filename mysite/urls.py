# This will be have basically the URLs which is all for Django projects, all the URLs will be rooted.

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

# This urls.py file is built by Django automatically.
# And this urlpatterns contains all the urls of the blog app.
# In other words, with each app you create, they should be declared in this urlpattern.

# '' empty string means home directory.
# When home directory is visited, /dogs is written by the user in the address bar of the browser.
# And this dogs is defined by the blog.urls
# blog is the name of the folder inside django_blog_translator folder
# urls is the name of the urls.py file of the blog app (blog folder)

# if you write, let's say myblog inside of the empty string, Django would be expecting:
# example.com/myblog/dogs     NOT example.com/dogs
# Lastly, include should be imported (line21)