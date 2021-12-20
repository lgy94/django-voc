from django.urls import path

from categoryapp.views import CategoryCreateView,  CategoryListView

app_name = 'categoryapp'

urlpatterns  = [

    path('create/', CategoryCreateView.as_view(), name='create'), #class베이스 view
    path('list/', CategoryListView.as_view(), name='list'),  # class베이스 view
    #path('test/', categoryapp.views.test, name='test'),

]
