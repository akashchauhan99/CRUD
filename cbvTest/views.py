from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student
from django.views.generic.base import RedirectView, TemplateView
from django.views import View

# Create your views here.

#This will add and show the data
class UserAddandShow(View):
    template_name = 'cbvTest/addandshow.html'
    def get(self, request, *args, **kwargs):
        # context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = Student.objects.all()
        context = {
            'stu':stud,
            'form':fm,
        }
        return render(request, 'cbvTest/addandshow.html', context)
    
    def post(self, request):
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
            return HttpResponseRedirect('/cbvtest/')
    
class UserDeleteView(RedirectView):
    url = '/cbvtest/'
    def get_redirect_url(self, *args, **kwargs):
        # print(args)
        print(kwargs)

        #Delete through object
        # stud_del = Student.objects.get(pk=kwargs['pk'])
        # stud_del.delete()

        #Delete directly
        Student.objects.get(pk=kwargs['pk']).delete()

        return super().get_redirect_url(*args, **kwargs)

class UserUpdateView(View):
    def get(self, request, **kwargs):
        stud = Student.objects.get(pk=kwargs['pk'])
        fm = StudentRegistration(instance=stud)
        context = {
            'form':fm
        }
        return render(request, 'cbvTest/updatestudent.html', context)
    
    def post(self, request, **kwargs):
        stud = Student.objects.get(pk=kwargs['pk'])
        fm = StudentRegistration(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
        context = {
            'form':fm
        }
        return render(request, 'cbvTest/updatestudent.html', context)
