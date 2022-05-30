from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .model import *
from django.http import HttpResponse


#Writing views

@login_required(login_url='/admin')
def index(request):
    if request.method == "POST" and request.POST['query']:
        q = request.POST['query']
        data = Applicant_Data.objects.filter(Q(nid__contains=q)|Q(status__contains=q)|Q(added_by__username__contains=q)|Q(date__contains=q)|Q(pk__contains=q)).order_by('-id')
        return render(request,"index.html",{"records":data})
    else:
        data = Applicant_Data.objects.all().order_by('-id')
        return render(request,"index.html",{"records":data})

@login_required(login_url='/admin')
def add_data(request):
    if request.method == "POST" and request.POST['nid']:
        userlist = User.objects.all()
        try:
            nid = request.POST['nid']
            status = request.POST['status']
            if request.user.is_superuser:
                user = request.POST['added_by']
                user = User.objects.get(username=user)
            else:
                user = request.user
            Applicant_Data.objects.create(nid=nid,status=status,added_by=user).save()
            return render(request,'add_data.html',{"info":"New Record Added Successfully.","userlist":userlist})
        except Exception as error:
            return render(request,'add_data.html',{"info":f"Something went wrong! {error}","userlist":userlist})
    else:
        userlist = User.objects.all()
        return render(request,'add_data.html',{"userlist":userlist})

