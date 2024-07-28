from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Star
from .forms import StarForm
from .serializers import StarSerializer


def index(request):
    return render(request, 'stars/index.html', {
        'stars': Star.objects.all()
    })


def view_star(request, id):
    return HttpResponseRedirect(reverse('index'))


#CRUD functions
def add(request):
    if request.method == 'POST':
        form = StarForm(request.POST)
        if form.is_valid():
            new_star_name = form.cleaned_data['star_name']
            new_star_constellation = form.cleaned_data['star_constellation']
            new_star_type = form.cleaned_data['star_type']
            new_star_distance = form.cleaned_data['star_distance']
            new_star_mass = form.cleaned_data['star_mass']
            new_star_temperature = form.cleaned_data['star_temperature']
            new_star_period = form.cleaned_data['star_period']
            new_star_turn_speed = form.cleaned_data['star_turn_speed']
        
            new_star = Star(
                star_name=new_star_name,
                star_constellation=new_star_constellation,
                star_type=new_star_type,
                star_distance=new_star_distance,
                star_mass=new_star_mass,
                star_temperature=new_star_temperature,
                star_period=new_star_period,
                star_turn_speed=new_star_turn_speed
            )
            new_star.save()
            return render(request, 'stars/add.html', {
                'form': StarForm(),
                'success': True
            })   
        else:
            return HttpResponseRedirect(reverse('index'))
        
    #Getting add page
    else:
        try:
            form = StarForm()
            return render(request, 'stars/add.html', {
            'form': StarForm()
            })
        except(ValueError):
            return HttpResponseRedirect(reverse('index'))


def edit(request, id):
    if request.method == 'POST':
        star = Star.objects.get(pk=id)
        form = StarForm(request.POST, instance=star)
        if form.is_valid():
            form.save()
            return render(request, 'stars/edit.html', {
                'form': form,
                'success': True
            })
    else:
        star = Star.objects.get(pk=id)
        form = StarForm(instance=star)
    return render(request, 'stars/edit.html', {
        'form': form,
        })


def delete(request, id):
    if request.method == 'POST':
        try:
            star = Star.objects.get(pk=id)
            star.delete()
            return HttpResponseRedirect(reverse('index'))
        except(ValueError):
            return HttpResponseRedirect(reverse('index'))


#DRF functions
#~/stars/
@csrf_exempt
def star_list(request):
    if request.method == 'GET':
        star = Star.objects.all()
        serializer = StarSerializer(star, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def star_detail(request, pk):
    try:
        star = Star.objects.get(pk=pk)
    except Star.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StarSerializer(star)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StarSerializer(star, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        star.delete()
        return HttpResponse(status=204)