from  django.conf.urls import patterns, url
urlpatterns = patterns('', 
     url(r'^accueil/$', 'blog.views.home'), # Accueil
 #    url(r'^article/(\d+)/$', 'view_article'),
 #    url(r'^articles/(\d{4})/(\d{2})/$', 'list_articles'), # vue des article d'un mois précis
 #    url(r'^$', 'tpl'),
)

