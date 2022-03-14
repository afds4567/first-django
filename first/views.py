from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from datetime import datetime
import random

def index(request):
    #template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html',context)
    #return HttpResponse(template.render(context, request))


def select(request):
    context = {}
    return render(request,'first/select.html',context)


def result(request):
    chosen = int(request.GET['number2'])
    results=[]
    if chosen>=1 and chosen <=45:
        results.append(chosen)

    box=[]
    for i in range(0,45):
        if chosen != i+1:
            box.append(i+1)
    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers' : results
    }
    return render(request, 'first/result.html', context)