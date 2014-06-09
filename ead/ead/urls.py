from django.conf.urls import patterns, include, url
from catch import views

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ead.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^begin/$', views.begin),
    url(r'^list/$', views.list),
    url(r'^sell/$', views.sell),
    url(r'^total/$', views.total),
)
