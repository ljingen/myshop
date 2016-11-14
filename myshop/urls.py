#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^shop/',include('shop.urls', namespace='shop')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

print('----DEBUG: depot 系统的url已被调用')