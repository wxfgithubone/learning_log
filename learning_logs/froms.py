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
        labels = {'st_name': '', 'age': '', 'sex': '',
                  'phone': '', 'home': ''}


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['course', 'score']
        labels = {'course': '', 'score': ''}
























