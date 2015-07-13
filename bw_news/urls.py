from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from newscaster import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bw_news.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include(urls.urlpatterns)),
)
