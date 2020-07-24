from django.urls import path
from myapp import views

urlpatterns = [
    path('demo1',views.demo1,name='demo1'),
    path('demo2',views.demo2,name='demo2'),
    path('fact/<n>',views.fact,name='fact'),
    
]

