from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('app.views',
    url('^$', views.index, name="index"),
    url('^(?P<application_id>[0-9]+)/$', views.deploy, name='deploy'),
)
