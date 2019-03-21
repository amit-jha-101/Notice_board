from django.db import models

# Create your models here.


class TeacherNotices(models.Model):
    teacherName = models.CharField(max_length = 255)
    noticeTitle = models.CharField(max_length = 255)
    noticeSubject = models.TextField(blank = True, null = True)
    #noticePdf = models.FileField(upload_to='notice/',blank = True, null = True)
    noticUrl = models.TextField(blank=True, null= True )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 255, default = "PENDING")
    description = models.TextField(blank=True, null = True)
    notice_id = models.AutoField(primary_key = True)

    def __str__(self):
        return "Teacher name = "+str(self.teacherName)+", notice = "+str(self.noticeTitle)+", notice-subject = "+str(self.noticeSubject)
            