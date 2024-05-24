from django.shortcuts import render,redirect
from myapp.models import employee
from myapp.forms import empform
import sys

# Create your views here.
def show(request):
    e=employee.objects.all()
    return render(request,"show.html",{'employees':e})

def empdelete(request,id):
    e=employee.objects.get(eid=id)
    e.delete()
    return redirect("/show")

def empinsert(request):
    if request.method=="POST":
        form=empform(request.POST)
        print("---------",form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                print("--------------",sys.exc_info())
    else:
        return render(request,'insert.html')