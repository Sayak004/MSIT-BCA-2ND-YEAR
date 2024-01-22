from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="home"),
    path('tirtho',views.page1,name="page_one")
]