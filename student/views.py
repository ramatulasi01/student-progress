from django.shortcuts import get_object_or_404, render
from student.models import Studentprogress

def student_detail(request,pk):
    student=get_object_or_404(Studentprogress,pk=pk)
    context={
        'student':student,
    }
    return render(request,'student_detail.html',context)



