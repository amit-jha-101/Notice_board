from django.shortcuts import render,redirect
from teacher.models import TeacherNotices
# Create your views here.

def dataView(request):
    x = TeacherNotices.objects.all().filter(status = "PENDING")
    
    listed = []
    name = []
    ids = []
    for e in x:
        data = {}
        data['noticeTitle'] = e.noticeTitle
        data['noticeSubject'] = e.noticeSubject
        data['description'] = e.description
        data['noticUrl'] = e.noticUrl
        data['teacherName'] = e.teacherName
        data['notice_id'] = e.notice_id
        listed.append(data)
        name.append(data['noticeTitle'])
        ids.append(data['notice_id'])
    context={}
    context['data'] = listed
    context['name'] = name
    context['ids'] = ids
    print(str(context))
    
        

    return render(request, 'hod/home.html', context = context)

def formView(request):
    if request.method == 'POST':
        print(request.POST.copy())
        keys = request.POST.copy().keys()
        data = request.POST.copy()
        print(keys)
        for key in keys:
            if key == 'csrfmiddlewaretoken':
                pass
            else:
                a = TeacherNotices.objects.filter(notice_id = key).first()
                a.status = data[key]
                a.save(update_fields = ['status'])
                


        return redirect('hod-home')