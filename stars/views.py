from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect # do i need this?????
from django.urls import reverse

from .models import Star
from .forms import StarForm


# Create your views here.
def index(request):
    return render(request, 'stars/index.html',{
        'stars': Star.objects.all()
    })


def view_star(request, id):
    star = Star.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


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
                star_name = new_star_name,
                star_constellation = new_star_constellation,
                star_type = new_star_type,
                star_distance = new_star_distance,
                star_mass = new_star_mass,
                star_temperature = new_star_temperature,
                star_period = new_star_period,
                star_turn_speed = new_star_turn_speed
            )
            new_star.save()
            return render(request, 'stars/add.html', {
                'form': StarForm(),
                'success': True
            })
        else:
            form = StarForm()
        return render(request, 'stars/add.html', {
            'form': StarForm()
        })

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
        star = Star.objects.get(pk=id)
        star.delete()
    return HttpResponseRedirect(reverse('index'))
