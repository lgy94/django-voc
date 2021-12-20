from django.urls import path
from django.views.generic import TemplateView

from vocapp.views import hello_world, VocCreatView, VocDetailView, VocUpdateView, VocDeleteView, VocListView, \
    downolad_excel

app_name = "vocapp" # vocapp:helloworld와 같이 나중에 쓸일이 생김

urlpatterns=[

    path('hello_world/', hello_world, name='hello_world'), #함수형view
    path('create/', VocCreatView.as_view(), name='create'), #class베이스 view
   #path('create/', test, name='create'), #class베이스 view


    path('detail/<int:pk>', VocDetailView.as_view(), name='detail'), #class베이스 view
    path('update/<int:pk>', VocUpdateView.as_view(), name='update'),  # class베이스 view
    path('delete/<int:pk>', VocDeleteView.as_view(), name='delete'),  # class베이스 view
    path('list/<int:pk>',VocListView.as_view(), name='list'),

    path('text/', downolad_excel, name='test'),

]