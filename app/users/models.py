# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class Group(models.Model):
    name = models.CharField('名称', max_length=10, unique=True)
    desc = models.CharField('描述', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = '用户组'
        verbose_name_plural = verbose_name
        ordering = ['id',]

    def __str__(self):
        return self.name


class Member(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', '管理员'),
        ('User', '普通用户'),
    )
    role = models.CharField('角色', max_length=5, choices=ROLE_CHOICES, default='User')
    email = models.EmailField('邮箱', unique=True)
    group = models.ManyToManyField(Group, verbose_name='用户组')
    avatar = models.ImageField('头像', upload_to='avatar/%Y/%m/%d', blank=True, null=True)
    rsakey = models.CharField('私钥', max_length=5000)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id',]

    def __str__(self):
        return self.username
