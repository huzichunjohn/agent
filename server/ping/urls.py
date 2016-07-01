from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('ping.views',
    url('^$', views.index, name="index"),
    url('^status/$', views.status, name="status"),
)
