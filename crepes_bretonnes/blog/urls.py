from  django.conf.urls import patterns, url, include
urlpatterns = patterns('blog.views', 
     url(r'^accueil/$', 'home'),
     url(r'^truc/$', 'truc'),
     url(r'^chose/$', 'chose'),
     url(r'^foo/$', 'foo'),
)

