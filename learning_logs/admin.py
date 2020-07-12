from django.contrib import admin

# 在这里注册你的模型

from learning_logs.models import Topic, Entry, Img2, StudentMessage, StudentCourse

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Img2)
admin.site.register(StudentMessage)
admin.site.register(StudentCourse)
