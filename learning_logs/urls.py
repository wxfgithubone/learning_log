# 定义learning_logs的URL模式

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # 说明
    url(r'^$', views.state, name='state'),

    # 主页
    url(r'^index/$', views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 编辑主题
    url(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # 用于删除条目
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry'),

    # 添加图片
    url(r'^add_img/$', views.add_img, name='add_img'),
    # 查看图片
    url(r'^look_img/$', views.look_img, name='look_img'),
    # 删除图片
    url(r'^del_img/(?P<id>\d+)/$', views.del_img, name='del_img'),

    # 显示所有学生
    url(r'^students/$', views.students, name='students'),
    # 学生的详细页
    url(r'^student/(?P<student_id>\d+)/$', views.student, name="student"),
    # 添加学生
    url(r'^add_student/$', views.add_student, name="add_student"),
    # 添加课程
    url(r'^add_course/(?P<student_id>\d+)/$', views.add_course, name="add_course"),
    # 修改学生信息
    url(r'^update_student/(?P<student_id>\d+)/$', views.update_student, name="update_student"),
    # 修改学生成绩
    url(r'^update_course/(?P<studentcourse_id>\d+)/$', views.update_course, name="update_course"),
    # 用于删除成绩
    # url(r'^del_course/(?P<studentcourse_id>\d+)/$', views.del_course, name='del_course'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


