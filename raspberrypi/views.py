from django.shortcuts import render
from teacher.models import TeacherNotices
# Create your views here.
def showNotice(request):
    t = TeacherNotices.objects.filter(status = "Accepted")
    context = {}
    context['data'] = t
    return render(request,'raspberrypi/home.html',context)

    