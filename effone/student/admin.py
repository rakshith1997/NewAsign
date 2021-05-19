from django.contrib import admin

from .models import Student, Profile, MyModel

admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(MyModel)
