from django.shortcuts import render

# Create your views here.
def index(r):
    context_dict={'text':'hello world','number':100}
    return render(r,'basic_app/index.html',context_dict)

def other(r):
    return render(r,'basic_app/other.html')

def relative(r):
    return render(r,'basic_app/relative_url_templates.html')
