# 序列化
from django.contrib.auth.models import User, Group
from learning_logs.models import Topic, Entry, Img2, StudentMessage, StudentCourse
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"


class Img2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Img2
        fields = "__all__"


class StudentMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentMessage
        fields = "__all__"


class StudentCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentCourse
        fields = "__all__"



