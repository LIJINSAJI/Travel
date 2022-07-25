from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
