from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls'))
    # url(r'^accueil/$', 'blog.views.home'),
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^crepes_bretonnes/', include('crepes_bretonnes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
