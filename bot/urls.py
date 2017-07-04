from django.conf.urls import url
from django.contrib import admin

from index import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<race_id>\d+)/$', views.index),
]
