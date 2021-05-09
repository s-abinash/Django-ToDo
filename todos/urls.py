from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^details/(?P<id>\w{0,50})/$', views.details),
	url(r'^removetodo/(?P<id>\w{0,50})/$', views.remove),
	url(r'^edit/(?P<id>\w{0,50})/$', views.edit, name='edit' ),
	url(r'^add', views.add, name='add'),
]