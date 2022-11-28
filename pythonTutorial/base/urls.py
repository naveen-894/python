from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('createRoom/',views.CreateRoom,name='createRoom'),
    path('updateRoom/<str:roomId>/',views.updateRoom,name='updateRoom'),
    path('deleteRoom/<str:roomId>/',views.deleteRoom,name='deleteRoom')
]
