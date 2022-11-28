from email.charset import QP
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
from django.db.models import Q
from django.db.models import Count
def home(request):
    q= request.GET.get('searchTerm') if request .GET.get('searchTerm')!=None else ''
    print('the value is ',request.GET)
    # data=Room.objects.filter(topic__name__icontains=q)
    data=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    print(data)
    room_count=data.count()
    return render(request,'home.html',{'rooms':data,'room_count':room_count})
def about(request):
    return HttpResponse('about')
def CreateRoom(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'index.html',context)

def updateRoom(request,roomId):
    print(request.POST)
    room=Room.objects.get(id=roomId)
    form=RoomForm(instance=room)
    if request.POST:
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'form':form})

def deleteRoom(request,roomId):
    form=Room.objects.get(id=roomId)
    form.delete()
    return redirect('home')

# Create your views here.
