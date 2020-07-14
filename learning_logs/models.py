from django.db import models
from django.contrib.auth.models import User
# 在这里创建模型


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        if self.text <= self.text[:49]:
            return self.text[:50]
        else:
            return self.text[:50] + '....'


class Img2(models.Model):
    name = models.CharField(max_length=50)
    headimg = models.FileField(upload_to="img2/")
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudentMessage(models.Model):
    """学生基础信息"""
    gender = (
        ('男', '男'), ('女', '女'), ('性别不详', '性别不详')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    st_name = models.CharField(max_length=25, verbose_name="学生姓名")
    age = models.CharField(max_length=10, verbose_name="学生年龄")
    sex = models.CharField(max_length=10, choices=gender, default=' ', verbose_name="学生性别")
    phone = models.CharField(max_length=11, unique=True,
                             error_messages={'unique': "手机号已存在，请更换"}, verbose_name="手机号")
    home = models.CharField(max_length=128, verbose_name="学生地址")

    def __str__(self):
        """返回学生姓名"""
        return self.st_name


class StudentCourse(models.Model):
    """学生分数表"""
    cus = (
        ('语文', '语文'), ('数学', '数学'), ('英语', '英语'), ('计算机', '计算机'),
        ('体育', '体育'), ('音乐', '音乐'), ('美术', '美术'), ('古语', '古语'),
    )
    student = models.ForeignKey(StudentMessage, on_delete=models.CASCADE)
    course = models.CharField(max_length=10, choices=cus, default=' ', verbose_name='课程')
    score = models.IntegerField(max_length=10, verbose_name="分数")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "科目：{0}\n 分数：{1}".format(self.course, self.score)

