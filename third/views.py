from django.shortcuts import render,get_object_or_404,redirect
from third.models import Restaurant, Review
from django.core.paginator import Paginator
from third.forms import RestaurantFrom, ReviewForm
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


def update(request, restaurant_id):
    if request.method == 'POST' and restaurant_id is not None:
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = RestaurantFrom(request.POST, instance=item)
        if form.is_valid():
            new_item = form.save()
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id')) # third/update?id=2
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = RestaurantFrom(instance=item)
        return render(request, 'third/update.html', {'form':form})
    return HttpResponseRedirect('/third/list/')


def detail(request, restaurant_id):
    if restaurant_id is not None:
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html',{'item':item, 'reviews':reviews})
    return HttpResponseRedirect('/third/list/')


def delete(request, restaurant_id):
    if request.method == 'GET' and restaurant_id is not None:
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        item.delete()
    return HttpResponseRedirect('/third/list/')

def review_create(request, restaurant_id):
    #print("!!!!!!")
    if request.method == 'POST':
        #print("@@@@@")
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', restaurant_id=restaurant_id)

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant':item})
    return render(request, 'third/review_create.html', {'form':form, 'item':item })
