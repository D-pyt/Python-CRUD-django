from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        
    #If method!= 'POST'
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


#DRF functions(class format)
#~/stars/
class StarList(APIView):
    def get(self, request, format=None):
        star = Star.objects.all()
        serializer = StarSerializer(star, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StartDetail(APIView):
    def get_object(self, pk):
        try:
            return Star.objects.get(pk=pk)
        except Star.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        star = self.get_object(pk)
        serializer = StarSerializer(star)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        star = self.get_object(pk)
        serializer = StarSerializer(star, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        star = self.get_object(pk)
        star.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    