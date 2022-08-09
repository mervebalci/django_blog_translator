from django.shortcuts import render

# Create your views here.

def translator_view(request):
    return render(request, 'translator.html')

# This gets a request as parameter. So this function on the background it expects a request.
# And the URL here, will pass that request object when the user visits the website.
# Then return render, which it is imported.
# So render is a function which expects a request and template name which is translator.html