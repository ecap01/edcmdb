from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/token/$', obtain_auth_token, name='api-token'),
]
