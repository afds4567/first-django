from django.shortcuts import render, get_object_or_404
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestuarantForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants,5)

    page = request.GET.get('page')## third/list?page=1
    items = paginator.get_page(page)

    context = {
        'restaurants' : items
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestuarantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestuarantForm()
    return render(request, 'third/create.html', {'form' : form})


def update(request, id):
    if request.method == 'POST' and id is not None:
        #item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        form = RestuarantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        #item = Restaurant.objects.get(pk=request.GET.get('id')) ##third/update?id=2
        item = get_object_or_404(Restaurant, pk=id)
        form = RestuarantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=id)
        return render(request,'third/detail.html',{'item':item})
    return HttpResponseRedirect('/third/list/')


def delete(request, id):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=id)
        item.delete()
    return HttpResponseRedirect('/third/list/')