from django.shortcuts import render
from .models import Stars

# Create your views here.
def index(request):
    return render(request, 'stars/index.html',{
        'stars': Stars.objects.all()
    })
