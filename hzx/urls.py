"""bbb"""
from django.urls import path
from hzx import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hzx/<name>", views.hzx_howsgoing, name="hzx_howsgoing"),
]
