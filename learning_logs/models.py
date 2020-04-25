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


# class Asset(models.Model):
#     """
#     资产表
#     """
#     brand = models.CharField(verbose_name='品牌', max_length=32)
#     model = models.CharField(verbose_name='型号', max_length=32)
#     number = models.CharField(verbose_name='编号', max_length=32)
#     leader_time = models.DateTimeField(verbose_name='领用时间', max_length=32)
#     leader = models.CharField(verbose_name='领用人', max_length=32)
#     return_time = models.DateTimeField(verbose_name='归还时间', max_length=32, null=True)
#     other = models.CharField(verbose_name='备注', max_length=128, null=True)
#
#     def __str__(self):
#
#         return self.leader
#
#     class Meta:
#         verbose_name = "资产表"
#         verbose_name_plural = verbose_name


