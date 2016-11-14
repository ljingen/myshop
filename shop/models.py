#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
"""
name 类型的字段
slug 类型的简写
"""
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug =models.SlugField(max_length=200,db_index=True,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name ='category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])
"""
category 类目字段，外键
name  商品名称
slug  商品的简称
image 商品图片
description 商品的描述文案
price 商品价格信息
stock 商品可用哭惨
available 商品的售卖状态
created 商品的创建时间
updated 商品的更新时间
"""
class Product(models.Model):
    #ForeignKey.related_name 这个名称可以用于让关联的对象反查到源对象，
    category = models.ForeignKey(Category,related_name='products')
    name = models.CharField(max_length =200,db_index=True)
    slug =models.SlugField(max_length=200,db_index=True)
    #Field.blank 如果为True 则该字段允许为空白，如果不填则不允许为空白，默认值为False
    image =models.ImageField(upload_to ='products/%Y/%m/%d',blank=True)
    description =models.TextField(blank=True)
    price =models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        index_together =(('id','slug'),)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])