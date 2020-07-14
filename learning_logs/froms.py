from django import forms
from .models import Topic, Entry, StudentMessage, StudentCourse


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class AddForm(forms.Form):  # 表单类用以生成表单
    name = forms.CharField()
    headimg = forms.FileField()


class StudentMessageFrom(forms.ModelForm):
    class Meta:
        model = StudentMessage
        fields = ['st_name', 'age', 'sex', 'phone', 'home']
        labels = {'st_name': '学生姓名', 'age': '年龄', 'sex': '性别',
                  'phone': '手机号码', 'home': '家庭住址'}


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['course', 'score']
        labels = {'course': '课程名称', 'score': '分数'}

