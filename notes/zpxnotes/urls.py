
from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^login/$', views.mylogin, name='login'),
    # trying to set up custom authentication/login

	url(r'^index', views.index, name='index'),
    url(r'^edit', views.edit, name='edit'),
    url(r'^delete', views.delete, name='delete'),
 ]