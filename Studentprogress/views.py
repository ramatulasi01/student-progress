from django.shortcuts import render
from student.models import Studentprogress

def home(request):
    student=Studentprogress.objects.all()
    context={
        'student':student,
    }
    return render(request,'home.html',context)