# Admin will contain codes that has to do with the admin interface.

# After built the web page with Django, will add an option to be able to add blog posts from the admin interface.
# To do that, will need to have a username and password.
# And to create that, open virtual environment and type 'python manage.py createsuperuser'
# Then, run the server => 'python manage.py runserver'

# In Admin Interface, only able to create new users and groups but not posts.
# To do that, a model should be created/registered (line25) which is the Post model in models.py
# So, Post in models.py has to be imported.

from django.contrib import admin
from .models import Post


# In the ADMIN INTERFACE, to add more content beside on the title, which it was Post object (1)/Post object (2) before:
class PostAdmin(admin.ModelAdmin):
    # After created this class, it will expect a list_display variable and it should be a tuple with strings
    list_display = ('title', 'date_created', 'author')
# This class should be registered (line25) after it is created. Because till this class is registered, Django doesn't know about it.



# Register your models here.
admin.site.register(Post, PostAdmin)