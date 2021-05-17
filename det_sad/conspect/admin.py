from django.contrib import admin
from .models import *
# Register your models here.


class AnswerModelAdmin(admin.TabularInline):
    model = AnswerModel


class SubjectModelAdmin(admin.ModelAdmin):
    inlines = [AnswerModelAdmin]


admin.site.register(SubjectModel, SubjectModelAdmin)
# admin.site.register(AnswerModel, AnswerModelAdmin)
admin.site.register(LessonModel)
