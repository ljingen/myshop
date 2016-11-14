#coding:utf-8
# Create your views here.
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404
# app specific files

from .models import *
from .forms import *


def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CategoryForm()

    t = get_template('shop/create_category.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_category(request):
  
    list_items = Category.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('shop/list_category.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_category(request, id):
    category_instance = Category.objects.get(id = id)

    t=get_template('shop/view_category.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_category(request, id):

    category_instance = Category.objects.get(id=id)

    form = CategoryForm(request.POST or None, instance = category_instance)

    if form.is_valid():
        form.save()

    t=get_template('shop/edit_category.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('shop/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
"""
产品列表
@Time 2016/11/10
@参数 request category_slug=
"""
def product_list(request,category_slug=None):
    category = None

    categories =Category.objects.all()
    products =Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/product_list.html',
    {'category':category,'categories':categories,'products':products})
"""
产品属性页面
@Time 2016/11/11
@参数 request  id  slug
"""
def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'shop/product_detail.html',{'product':product})

def list_product(request):
    list_items = Product.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('shop/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_product(request, id):
    product_instance = Product.objects.get(id = id)

    t=get_template('shop/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request, id):

    product_instance = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance = product_instance)

    if form.is_valid():
        form.save()

    t=get_template('shop/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))