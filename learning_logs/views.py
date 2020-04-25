from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .froms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from learning_logs import models
from learning_log import mypage
# 在这里创建视图


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # topics = Topic.objects.order_by('date_added')
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



# @login_required
# def assets(request):
#     """显示所有的资产"""
#     # assets = Asset.objects.filter(owner=request.user).order_by('date_added')
#     # # topics = Topic.objects.order_by('date_added')
#     # context = {'assets': assets}
#     # return render(request, 'learning_logs/assets.html', context)
#     assets = models.Asset.objects.all()
#     print(assets)
#     # total_count = data_list.count()
#     #
#     # current_page = request.GET.get("page")
#     #
#     # page_boj = mypage.MyPage(current_page, total_count, url_prefix="asset/list")
#     # data = data_list[page_boj.start:page_boj.end]  # 从第几页显示到第几页
#     #
#     # page_html = page_boj.page_html()  # 页面
#     # page_num = page_boj.num()  # 序号
#     context = {'assets': assets}
#
#     return render(request, 'learning_logs/assets.html', context)


# def new_asset(request):
#     """
#     添加资产
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         form = AssetForm()
#         return render(request, 'asset_add.html', {'form': form})
#     form = AssetForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('/asset/list/')
#     return render(request, 'asset_add.html', {'form': form})
#
#
# def edit_asset(request, cid):
#     """
#     编辑资产
#     :return:
#     """
#     obj = models.Asset.objects.get(id=cid)
#     if request.method == 'GET':
#         form = AssetForm(instance=obj)
#         return render(request, 'asset_edit.html', {'form': form})
#     form = AssetForm(data=request.POST, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/asset/list/')
#     return render(request, 'asset_edit.html', {'form': form})


# def asset_del(request, cid):
#     """
#     删除资产
#     :param request:
#     :param cid:
#     :return:
#     """
#     # models.Asset.objects.filter(id=cid).delete()
#     #
#     # return redirect('/asset/list/')
#
#     origin = memory_reverse(request, 'asset_list')
#     print(origin)
#     if request.method == 'GET':
#         return render(request, 'delete.html', {'cancel': origin})
#     models.Asset.objects.filter(id=cid).delete()
#     return redirect(origin)

