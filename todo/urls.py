from django.conf.urls import patterns, include, url
from todo import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.to_do_list, name='todolist'),
    # url(r'^social_login$', views.social_login, name='social_login'),
    url(r'^add$', views.add_to_do, name='add_item'),
    url(r'^delete$', views.delete_item, name='delete_item'),
    url(r'^edit$', views.edit_item, name='edit_item'),
    # url('', include('social.apps.django_app.urls', namespace='social')),
   	url('', include('django.contrib.auth.urls', namespace='auth')),
   	url(r'^admin/', include(admin.site.urls)),
)