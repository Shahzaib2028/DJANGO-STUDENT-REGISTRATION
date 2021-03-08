from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            rl = fm.cleaned_data['roll_no']
            reg = User(name=nm , email=em , roll_no=rl)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, "enroll/addandshow.html" ,{'form': fm , 'stu' : stud})

def update_data(request, id):
    if request.method == "POST":
        pid = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pid)
        if fm.is_valid():
            fm.save()
    else:
        pid = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pid)
    return render(request, "enroll/updatestudent.html" , {'form': fm})


def delete_data(request, id):
    if request.method == "POST":
        pid = User.objects.get(pk=id)
        pid.delete()
        return HttpResponseRedirect("/")



