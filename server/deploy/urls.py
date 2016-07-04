from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'deploy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^ping/', include('ping.urls')),
    url(r'^application/', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
