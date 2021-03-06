from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Student)


################################################################
# 批量注册app名为api下的models到admin后台
################################################################

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
app_models = apps.get_app_config("oj").get_models()  # 获取app:api下所有的model,得到一个生成器
from oj.models import *
# 遍历注册model
for model in app_models:
    try:
        print(model)
        admin.site.register(model)
    except AlreadyRegistered:
        pass

admin.site.unregister(Student)
admin.site.unregister(Course)
admin.site.unregister(Question)
from django.forms import ModelForm, PasswordInput

class CustomStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'no', 'passwordd','classs','exams']
        widgets = {
            'passwordd': PasswordInput(),
        }

class StudentAdmin(admin.ModelAdmin):
    form = CustomStudentForm
    list_display = ("name","no","classs")

class CourseAdmin(admin.ModelAdmin):
    form = CustomStudentForm
    list_display = ("name","teacher")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "id", "author")

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)