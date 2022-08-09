from django.shortcuts import render

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        input_text = request.POST['my_textarea']
        output = input_text.upper()
        return render(request, 'translator.html', {'output_text':output, 'input_text':input_text})
    else:
        return render(request, 'translator.html')

# This gets a request as parameter. So this function on the background it expects a request.
# And the URL here, will pass that request object when the user visits the website.
# Then return render, which it is imported.
# So render is a function which expects a request and template name which is translator.html