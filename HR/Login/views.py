import abc
from os import name

from HR.settings import EMAIL_HOST_USER
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Panel_member, candidate, master_interview
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'testApp/base.html')


def handlelogin(request):
    if request.method == 'POST':
        username1 = request.POST['inputEmail']
        password = request.POST['inputPassword']
        user = auth.authenticate(username=username1, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dash')
        else:
            return redirect('/')


def handlelogout(request):
    auth.logout(request)
    return redirect('/')

def reg(request):
    if request.method == 'POST':
        Fname = request.POST['full_name']
        Age = request.POST['Age']
        Experience = request.POST['exp']
        Current_Company = request.POST['comp']
        email2 = request.POST['email2']
        skills = request.POST['message']
        cv = request.POST['file_cv']
        if len(Fname) < 2 or len(Age) < 1 or len(Age) > 3:
            messages.error(request, 'Please fill the form properly')
        else:
            candidate(Fullname=Fname, Age=Age, Experience=Experience,
                      Current_Company=Current_Company, Email=email2, Skills=skills, CV=cv).save()
            messages.success(request, 'The data is saved successfully')
            return redirect('index')
    return render(request, 'testApp/dash.html')

def indx(request):
    if request.method == "POST":
        Interview_rd = request.POST.get("Intrd")
        candidate_idid = request.POST.get("candidate")
        candidate_id = candidate.objects.get(id=candidate_idid)
        Job_position = request.POST.get("Jobpost")
        Status = request.POST.get("status")
        Panelmember_id = request.POST.get("panelmember")
        Panelmember = Panel_member.objects.get(id=Panelmember_id)
        feedback = request.POST.get("feedbk")
        ispromoted = request.POST.get("isp") or False
        master_interview.objects.create(Interview_rd=Interview_rd, candidate_id=candidate_id, Job_position=Job_position,
                                        Status=Status, Panelmember=Panelmember, feedback=feedback, ispromoted=ispromoted)
        subject = 'Interview Schedule'
        msg = "We would like to schedule a 2 round of phone call and video call with "+ candidate_id.Fullname +' ' +"Post:" +Job_position +' ' + "by" +' '+ Panelmember.Name +' '+ "at Trestlelinks private limited."
        to = [candidate_id.Email,Panelmember.Email]
        res= send_mail(subject, msg, settings.EMAIL_HOST_USER, to, fail_silently=False)
        if(res == 1):
            msg ="Assigned Successfully and Email Sent"
        else:
            msg = "Email not sent"
        return render(request,"testApp/final.html", {'masg':msg})
    else:
        return render(request, "testApp/index.html", {'candidatess': candidate.objects.all(),
                                                      'panel_members': Panel_member.objects.all()})


def dash1(request):
    return render(request, 'testApp/dash.html')


def succs(request):
    return render(request, 'testApp/final.html' )

def loginsuccess(request):
    return render(request, 'testApp/loginsuccess.html')

def candidatelogin(request):
    if request.method == 'POST':
        username2 = request.POST['inputEmail']
        password = request.POST['inputPassword']
        user = auth.authenticate(username=username2, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'testApp/loginsuccess.html', {'abc1':username2})
        else:
            return redirect('success')
    return render(request, 'testApp/candidate_login.html')
