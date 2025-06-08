from django.urls import path
from my_app import views

urlpatterns = [
    
    path ( 
        '' , views.About.as_view(), name = 'aboutpage'
    )
    ,
    path(
        'home' , views.HomePageView.as_view() , name = 'homepage'
    )
]