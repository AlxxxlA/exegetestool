from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add/$', views.add, name="add_references"),
    url(r'^display/(?P<position_id>[0-9]+)/$', views.display, name="display_references"),
    url(r'^update/(?P<position_id>.+)/$', views.update, name="update_references"),
    url(r'^display_yaml/$', views.display_yaml, name="display_yaml"),
]
