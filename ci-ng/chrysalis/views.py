from django.shortcuts import render

def index(request):
    return render(request, 'chrysalis/index.html')
