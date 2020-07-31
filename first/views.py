from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random
# Create your views here.

def index(request):
    # template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date':now
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'first/index.html', context)

def select(request):
    message = 'input a number: '
    context = {}
    return render(request, 'first/select.html',context)

def result(request):
    chosen = int(request.GET['number'])
    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    message = 'Result is : '
    context = {'numbers': results }
    return render(request, 'first/result.html',context)