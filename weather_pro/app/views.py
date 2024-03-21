from django.shortcuts import render, HttpResponse
from .app import wed_app, inp

def index(request):
    # return HttpResponse("this is tp")
    if request.method == 'POST':
        cit = str(request.POST['city'])
        inp(cit)
        tp = wed_app()
        wed = tp
        return render(request, 'index.html', {'weather': wed[0], 'temp': wed[4],'hum':wed[2], 'loc':wed[3], 'spd':wed[5]})
    return render(request, 'index.html')
