from django.contrib import admin
from .models import NoticeBoard
from main.models import question,answer
# Register your models here.
admin.site.register(NoticeBoard)
# Register your models here.
admin.site.register(question)
admin.site.register(answer)