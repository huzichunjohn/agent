from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('app.views',
    url('^$', views.index, name="index"),
)
