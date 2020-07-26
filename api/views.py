# 视图
from django.contrib.auth.models import User, Group
from learning_logs.models import \
    Topic, Entry, Img2, StudentMessage, StudentCourse
from rest_framework import viewsets
from api.serializers import \
    UserSerializer, GroupSerializer,\
    TopicSerializer, EntrySerializer, \
    Img2Serializer, StudentMessageSerializer,\
    StudentCourseSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """查看，编辑用户的界面"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """查看，编辑组的界面"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """查看主题"""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class EntryViewsSet(viewsets.ModelViewSet):
    """查看日记"""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class ImgViewsSet(viewsets.ModelViewSet):
    """查看图片"""
    queryset = Img2.objects.all()
    serializer_class = Img2Serializer


class StudentMessageViewsSet(viewsets.ModelViewSet):
    """学生信息"""
    queryset = StudentMessage.objects.all()
    serializer_class = StudentMessageSerializer


class StudentCourseViewsSet(viewsets.ModelViewSet):
    """学生成绩"""
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer





