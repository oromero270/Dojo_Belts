from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing ),
    path('sub', views.subuser ),
    path('subtrip', views.subtrip ),
    path('travels', views.homeview ),
    path('travels/add', views.newtravel),
    path('join/<tripid>', views.jointrip),
    path('travels/destination/<myid>', views.proof),
    path('login', views.security),
    path('logout', views.clearuser),

]
