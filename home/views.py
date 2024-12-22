from django.http import HttpResponse
from django.shortcuts import render

from course.models import Subject, Course, Tutor
from home.models import Setting


def index(request):
    setting=Setting.objects.get()
    subject_cr = Subject.objects.all().order_by('id')[:4]
    course_cr = Course.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[0:3]
    context={"setting":setting,
             "subject_cr":subject_cr,
             "course_cr":course_cr,
             "Tutor":tutor_cr,
             }
    return render(request, 'index.html',context)


def about(request):
    setting = Setting.objects.get()
    context = {"setting": setting,}
    return render(request, "about.html",context)


def contact(request):
    setting = Setting.objects.get()
    context = {"setting": setting}
    return render(request,"contact.html", context)

def tutor(request):
    setting = Setting.objects.get()
    tutor = Tutor.objects.all()
    context = {"setting": setting, 'tutor': tutor}
    return render(request,"tutors.html", context)


