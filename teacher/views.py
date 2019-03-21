from django.shortcuts import render,redirect
from .models import TeacherNotices
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from time import gmtime, strftime
# Create your views here.


def teacherHome(request):
    return render(request,'teacher/teacherHome.html',context={})

def teacherForm(request):
    if request.method == 'POST' and request.FILES['file']:
        data = request.POST.copy()
        print(data)
        files = request.FILES['file']
        #files.name = "x_"+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+".pdf"
        fs = FileSystemStorage()
        print(type(files))
        filename = fs.save(files.name,files)
        #print(files.keys())
        file_url = fs.url(filename)
        #f = data['file']
        #print(f)
        t = TeacherNotices(
            teacherName = "x",
            noticeTitle = data['noticeTitle'],
            noticeSubject = data['noticeSubject'],
            noticUrl = file_url,
            description = data['noticeDescription']
            )
        t.save()
        return redirect("teacher-home")

        
