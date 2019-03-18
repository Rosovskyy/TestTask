from django.conf.urls import url
from . import views

app_name = "groups"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<user_id>[-\w]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<user_id>[-\w]+)/delete/$', views.delete, name='delete'),
    url(r'^/add/', views.add, name="add"),
    url(r'^/addGroup/', views.addGroup, name="addGroup"),
    url(r'^(?P<group_id>[-\w]+)/editGroup/$', views.editGroup, name="editGroup"),
]