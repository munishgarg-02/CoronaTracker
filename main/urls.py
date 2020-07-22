from django.urls import path
from main import views

urlpatterns = [
    path('',views.Main,name="main"),
    path('details/<slug>',views.Detail,name='detail'),
    path('about',views.About,name="about")
]
