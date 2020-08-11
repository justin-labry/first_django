from django.shortcuts import render,get_object_or_404
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestaurantFrom
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()

    paginator = Paginator(restaurants, 4)

    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'restaurants': items,
    }

    return render(request, 'third/list.html', context)

def test(request):
    context = {

    }

    return render(request, 'third/test3.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantFrom(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestaurantFrom()
    return render(request, 'third/create.html', {'form':form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        form = RestaurantFrom(request.POST, instance=item)
        if form.is_valid():
            new_item = form.save()
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id')) # third/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantFrom(instance=item)
        return render(request, 'third/update.html', {'form':form})
    return HttpResponseRedirect('/third/list/')


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        return render(request, 'third/detail.html',{'item':item})
    return HttpResponseRedirect('/third/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/list/')