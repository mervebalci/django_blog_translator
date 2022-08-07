from . import views
# . means current location and views is a file but when you import things, it becomes a module
from django.urls import path
# urls is another module of Django and path is a function

urlpatterns = [
    path('', views.translator_view, name='translator_view')    # Empty strings '' represent the homepage
]

# By default, python works with functions such as .as_view()
# translator_view is a view, so no need as_view function here.