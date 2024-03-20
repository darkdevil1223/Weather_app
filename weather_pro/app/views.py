from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("this is home page ")
    return render(request, 'index.html')
