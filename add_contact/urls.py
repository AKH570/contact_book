from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('newcont/',views.newcontact,name='newcont'),
    path('allcont/',views.ContactList,name='allcont'),
    path('editcont/<int:pk>/',views.EditContuct,name='editcont'),
    path('deletecont/<int:pk>/',views.DeleteContuct,name='deletecont'),
    path('qmath/',views.QuickMath,name='qmath'),
    path('result/',views.Result,name='result'),
    path('calculator/',views.Calculator,name='calculator'),
    
]