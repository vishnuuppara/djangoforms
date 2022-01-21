from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('add/<int:a>/<int:b>',views.add,name='add'),
    path('intro/<str:name>/<int:age>',views.intro,name='intro'),
    path('firstpage',views.firstpage,name='firstpage'),
    path('secondpage',views.secondpage,name='secondpage'),
    path('thirdpage',views.thirdpage,name='thirdpage'),
    path('firstimg/<str:img>',views.firstimg,name='firstimg'),
    path('secondimg',views.secondimg,name='secondimg'),
    path('form2',views.form2,name='form2'),

]