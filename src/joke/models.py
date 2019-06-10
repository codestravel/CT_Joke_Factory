
from django.db import models

# Create your models here.
class User(models.Model):
    """ User - 用户表
    保存用户注册信息，登陆信息
    作者: 代码之间
    时间：2019.06.02
    """
    username = models.CharField(verbose_name = '用户名', max_length = 256, unique = True)
    password = models.CharField(verbose_name = '密码', max_length = 256, default='123456')
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = "用户管理"

class Category(models.Model):
    """ Category - 分类
    作者: 代码之间
    时间：2019.06.10
    """
    name = models.CharField(verbose_name='类别名', max_length=512)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "类别管理"
        verbose_name_plural = "类别管理"
    
class Joke(models.Model):
    """ Joke - 笑话表
    保存笑话
    作者: 代码之间
    时间：2019.06.10
    """
    title = models.CharField(verbose_name = '标题', max_length = 512)
    content = models.TextField(verbose_name = '内容')
    # auto_now_add 字段表示，创建时由系统自动加上，以后不能更改
    date = models.DateTimeField(verbose_name='发布时间', auto_now_add=True) 
    # 发布者（贡献者）， 级联删除
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    # 分类
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "笑话管理"
        verbose_name_plural = "笑话管理"








