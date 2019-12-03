# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mistune

from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.utils.html import format_html

import task
from task.models import TaskCategory



class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, verbose_name="责任人", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="责任人", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '标签'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    ISSUE_STATUS_OK = 0
    ISSUE_STATUS_NOK = 1
    ISSUE_STATUS_ITEMS = (
        (ISSUE_STATUS_OK, 'OK'),
        (ISSUE_STATUS_NOK, 'NOK'),

    )

    issue_no = models.CharField(default='xx1', max_length=255, verbose_name="问题编号")
    issue_status = models.CharField(max_length=50, verbose_name="问题状态")
    title = models.CharField(max_length=255, verbose_name="问题标题")
    week = models.CharField(max_length=1024, blank=True, verbose_name="会议周")
    agenda = models.CharField(max_length=1024,verbose_name="日程")
    start_time = models.CharField(max_length=1024, blank=True, verbose_name="开始时间")
    duration = models.CharField(max_length=1024, blank=True, verbose_name="持续时间")
    agenda_order = models.CharField(max_length=1024, blank=True, verbose_name="议程顺序")
    participants = models.CharField(max_length=1024, verbose_name="与会人")
    link = models.CharField(max_length=1024, blank=True, verbose_name="链接")
    task_code = models.CharField(max_length=1024, blank=True, verbose_name="任务编号")
    task_content = models.CharField(max_length=1024, blank=True, verbose_name="任务内容")
    # task_category = models.ForeignKey(TaskCategory, verbose_name="部门", on_delete=models.DO_NOTHING
    #                                   )

    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式")
    content_html = models.TextField(verbose_name="正文html代码", blank=True, editable=False)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    is_md = models.BooleanField(default=False, verbose_name="markdown语法")
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(User, verbose_name="责任人", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = verbose_name_plural = "Issue"
        ordering = ['-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_md:
            self.content_html = mistune.markdown(self.content)
        else:
            self.content_html = self.content
        super().save(*args, **kwargs)

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')
        return post_list, category

    @classmethod
    def latest_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL)

    @classmethod
    def hot_posts(cls):
        result = cache.get('hot_posts')
        if not result:
            result = cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')
            cache.set('hot_posts', result, 10 * 60)
        return result

    def blog_color_state(self):
        if self.issue_status == 'NOK':
            font_code = 'white'
            color_code = '#EE6A50'
            assign_state_name = 'NOK'

        # elif self.issue_status == '':
        #     font_code = '#EE9572'
        #     color_code = 'yellow'
        #     assign_state_name = '进 行 中'
        else:
            font_code = 'white'
            color_code = 'green'
            assign_state_name = 'OK'
        return format_html(
            '<span style="color:{}; background:{};font-weight: 520;">{}</span>',
            font_code,
            color_code,
            assign_state_name,
        )

    blog_color_state.short_description = '完成状态'

