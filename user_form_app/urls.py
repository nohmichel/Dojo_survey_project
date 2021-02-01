from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # path('result', views.front_page),
    path('result', views.result_index),	   
]