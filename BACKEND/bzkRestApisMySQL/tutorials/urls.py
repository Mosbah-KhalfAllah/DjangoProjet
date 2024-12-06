from django.urls import path 
from tutorials import views 
 
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
    
]
