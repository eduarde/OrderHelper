from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pending_comanda, name='pending_comanda'),
    url(r'^comanda/(?P<pk>[0-9]+)/$', views.comanda_subcomenzi, name='comanda_subcomenzi'),
    url(r'^persoana/new/$', views.persoana_new, name='persoana_new'),
    url(r'^add_home$', views.add_home, name='add_home'),
]