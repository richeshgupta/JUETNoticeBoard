from django.contrib import admin
from .models import NoticeBoard
from main.models import question,answer,reportques,reportans
# Register your models here.
admin.site.register(NoticeBoard)
# Register your models here.
admin.site.register(question)
admin.site.register(answer)
admin.site.register(reportques)

admin.site.register(reportans)