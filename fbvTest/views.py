from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

#This will add and show the data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            #Save using form object
            # fm.save()
            #Save using model object
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    context = {
        'form':fm,
        'stu':stud,
    }
    return render(request, 'fbvtest/addandshow.html', context)

#This function will delete the data
def delete_data(request, pk):
    if request.method == 'POST':
        st_del = Student.objects.get(pk=pk)
        st_del.delete()
        return HttpResponseRedirect('/fbvtest/')

def update_data(request, pk):
    if request.method == 'POST':
        stud = Student.objects.get(pk=pk)
        fm = StudentRegistration(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
    else:
        stud = Student.objects.get(pk=pk)
        fm = StudentRegistration(instance=stud)
    context = {
            'form':fm
    }
    return render(request, 'fbvtest/updatestudent.html', context)
