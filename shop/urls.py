#coding:utf-8
from django.conf.urls import url
from .models import *
from .views import *
app_name = "shop"
urlpatterns =[
    url(r'^$',product_list,name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',product_detail,name='product_detail'),
    url(r'^category/create/$', create_category, name='create_category'),
    url(r'^category/list/$', list_category, name='list_category'),
    url(r'^category/edit/(?P<id>[^/]+)/$', edit_category, name='edit_category'),
    url(r'^category/view/(?P<id>[^/]+)/$', view_category, name='view_category'),
    url(r'^product/create/$', create_product, name='create_product'),
    url(r'^product/list/$', list_product, name='list_product'),
    url(r'^product/edit/(?P<id>[^/]+)/$', edit_product, name='edit_product'),
    url(r'^product/view/(?P<id>[^/]+)/$', view_product, name='view_product'),    
]