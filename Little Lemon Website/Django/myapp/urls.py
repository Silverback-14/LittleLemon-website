from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('menu/<str:dish>', views.menu),
    path('home/forms',views.form_view),
    path('about/',views.about),
    
]
