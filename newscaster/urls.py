from django.conf.urls import url

from . import views

urlpatterns = [ url(r'([a-zA-Z0-9_.-]*)$', views.render_article)]