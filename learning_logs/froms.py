from django import forms
from .models import Topic, Entry


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


# class AssetForm(forms.ModelForm):
#     class Meta:
#         model = Asset
#         fields = "__all__"
#
#     def __init__(self, *args, **kwargs):
#
#         super(AssetForm, self).__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'  # 应用样式
#             field.widget.attrs['placeholder'] = field.label  # 默认显示的字段
#         # self.fields['brand'].empty_label = "请选择品牌"
#         self.fields['other'].required = False
#         self.fields['return_time'].required = False























