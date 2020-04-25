# 定义learning_logs的URL模式

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),


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
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry')

    # # 显示所有的资产表
    # url(r'^assets/$', views.assets, name='assets'),
    # # 新增资产表
    # url(r'^new_asset/(?P<asset_id>\d+)/$', views.new_asset, name='new_asset'),
    # # 编辑资产表
    # url(r'^edit_asset/(?P<asset_id>\d+)/$', views.edit_asset, name='edit_asset'),

]








