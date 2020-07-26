"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# 路由
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.GroupViewSet, basename='group')
router.register(r'topics', views.TopicViewSet, basename='topic')
router.register(r'entry', views.EntryViewsSet, basename='entry')
router.register(r'img', views.ImgViewsSet, basename='img2')
router.register(r'StudentMessage', views.StudentMessageViewsSet, basename='studentmessage')
router.register(r'StudentCourse', views.StudentCourseViewsSet, basename="studentcourse")


schema_view = get_schema_view(title="Learning API",
                              url="http://localhost:8000/docs/",
                              description="这里是介绍",
                              renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^docs/', schema_view, name="docs"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('learning_logs.urls', namespace='learning_logs')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
