from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
import bcrypt
from django.db.models import Q

def landing (request):
    return render (request,'login_page.html')

def security (request):
    errorsmade = users.objects.login_validator(request.POST)
    if len(errorsmade) > 0 :
        for key, value in errorsmade.items():
            messages.error(request, value)
        return redirect(f'/')
    else:
        account=users.objects.get(username = request.POST['uname'])
        request.session['loggedinId'] = account.id
        return redirect ('/travels')

def subuser (request):
    errorsmade = users.objects.basic_validator(request.POST)
    if len(errorsmade) > 0 :
        for key, value in errorsmade.items():
            messages.error(request, value)
        return redirect(f'/')
    else:
        pwhash=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        newuser =users.objects.create(first_name = request.POST['name'],username =request.POST['uname'] , password = pwhash)
        request.session['loggedinId'] = newuser.id
        return redirect ('/travels')

def subtrip (request):
    errorsmade = trips.objects.newtrip_validator(request.POST)
    if len(errorsmade) > 0 :
        for key, value in errorsmade.items():
            messages.error(request, value)
        return redirect(f'/travels/add')
    else:
        myaccount=users.objects.get(id= request.session['loggedinId'])
        newtrip =trips.objects.create(destination = request.POST['location'],description =request.POST['info'] , startdate = request.POST['sdate'], enddate = request.POST['edate'], uploader= myaccount)

        return redirect ('/travels')

def homeview (request):
    if 'loggedinId' not in request.session:
        return redirect ('/')
    else:
        activeuser = users.objects.get(id=request.session['loggedinId'])
        context = {
            'myinfo':activeuser,
            'mytrips':trips.objects.filter(Q(uploader = activeuser) | Q(attedning =activeuser)),
            'notmytrips':trips.objects.exclude(Q(uploader = activeuser) | Q(attedning =activeuser))
        }
        return render (request,'home.html', context)

def jointrip  (request,tripid):
    activeuser = users.objects.get(id= request.session['loggedinId'])
    jointrip= trips.objects.get(id= tripid)
    jointrip.attedning.add(activeuser)
    return redirect ('/travels')

def proof (request,myid):
    activeuser = users.objects.get(id=request.session['loggedinId'])
    location_info=trips.objects.get(id=myid)
    useraccount = users.objects.all()
    ontrip= location_info.attedning.exclude(id=activeuser.id)

    context = {
        'trip':location_info,
        'others':ontrip
    }
    return render (request,'location.html',context)


def  newtravel (request):
    return render (request,'add_trip.html')

def clearuser (request):
    request.session.clear()
    return redirect ('/')