from django.shortcuts import render

def home(request):
    context = {}
    template = 'index/home.html'
    return render(request, template, context)
