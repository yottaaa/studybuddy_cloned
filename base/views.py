from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def room(request, pk):
    context = {
        "room_id": pk
    }
    return render(request, 'base/room.html', context)
