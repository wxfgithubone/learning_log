from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from .models import Topic, Entry, Img2, StudentMessage, StudentCourse
from .froms import TopicForm, EntryForm, AddForm, StudentMessageFrom, StudentCourseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# 在这里创建视图.


@login_required
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


def state(request):
    """学习笔记说明"""
    return render(request, "learning_logs/state.html")


@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = get_object_or_404(Topic, id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def edit_topic(request, topic_id):
    """修改主题名称"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 初次请求，使用当前条目充当表单
        form = TopicForm(instance=topic)
    else:
        # post提交的数据，对数据进行处理
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'topic': topic, 'topics': topics, 'form': form}
    return render(request, 'learning_logs/edit_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题里添加新的条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = EntryForm()
    else:
        # post 提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前条目充当表单
        form = EntryForm(instance=entry)
    else:
        # post提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def del_entry(request, entry_id):
    """删除条目"""
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return render(request, 'learning_logs/index.html')


@login_required
def add_img(request):
    """添加图片"""
    # 判断是否为 post 方法提交
    if request.method == "POST":
        af = AddForm(request.POST, request.FILES)
        # 判断表单值是否和法
        if af.is_valid():
            name = af.cleaned_data['name']
            headimg = af.cleaned_data['headimg']
            img = Img2(name=name, headimg=headimg)
            img.owner = request.user
            messages.error(request, '添加图片成功')
            img.save()
            return render(request, 'learning_logs/look_img.html', context={"img": img})
    else:
        af = AddForm()
        return render(request, 'learning_logs/add_img.html', context={"af": af})


@login_required
def look_img(request):
    """查看当前用户的图片"""
    imgs = Img2.objects.filter(owner=request.user).order_by('-date_added')
    context = {"imgs": imgs}
    return render(request, 'learning_logs/imgs.html', context)


@login_required
def del_img(request, id):
    """删除图片"""
    img = Img2.objects.get(id=id)
    img.delete()
    return render(request, 'learning_logs/index.html')


def students(request):
    """显示所有学生"""
    students = StudentMessage.objects.filter(owner=request.user).order_by('-date_added')
    context = {"students": students}
    return render(request, 'learning_logs/students.html', context)


def student(request, student_id):
    """单个学生的成绩页"""
    student = get_object_or_404(StudentMessage, id=student_id)
    if student.owner != request.user:
        raise Http404
    st = student.studentcourse_set.order_by('-date_added')
    context = {'student': student, 'st': st}
    return render(request, 'learning_logs/student.html', context)


def add_student(request):
    """添加学生"""
    if request.method != 'POST':
        form = StudentMessageFrom()
    else:
        form = StudentMessageFrom(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.owner = request.user
            new_student.save()
            return HttpResponseRedirect(reverse('learning_logs:students'))

    context = {'form': form}
    return render(request, 'learning_logs/add_student.html', context)


@login_required
def update_student(requests, student_id):
    """修改学生信息"""
    student = StudentMessage.objects.get(id=student_id)
    if requests.method != 'POST':
        form = StudentMessageFrom(instance=student)
    else:
        form = StudentMessageFrom(instance=student, data=requests.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:students"))
    context = {"student": student, "students": students, "form": form}
    return render(requests, "learning_logs/update_student.html", context)


def add_course(request, student_id):
    """指定学生的成绩"""
    student = StudentMessage.objects.get(id=student_id)
    if request.method != 'POST':
        form = StudentCourseForm()
    else:
        form = StudentCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.student = student
            new_course.save()
            return HttpResponseRedirect(reverse('learning_logs:student', args=[student_id]))
    context = {'student': student, 'form': form}
    return render(request, 'learning_logs/add_course.html', context)


def update_course(request, studentcourse_id):
    """编辑学生成绩"""
    course = StudentCourse.objects.get(id=studentcourse_id)
    student = course.student
    if student.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = StudentCourseForm(instance=course)
    else:
        form = StudentCourseForm(instance=course, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:student"), args=[student.id])
    context = {"course": course, "student": student, "form": form}
    return render(request, "learning_logs/update_course.html", context)


# @login_required
# def del_course(request, studentcourse_id):
#     """删除成绩"""
#     course = StudentCourse.objects.get(id=studentcourse_id)
#     course.delete()
#     return render(request, 'learning_logs/index.html')

