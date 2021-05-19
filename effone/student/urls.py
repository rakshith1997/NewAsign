from django.contrib import admin
from django.urls import path
from .views import StudentDetail, StudentList, StudentCreate, StudentDelete

app_name = 'student'

urlpatterns = [
    path('list/', StudentList.as_view(), name='list'),
    path('detail/<int:pk>/', StudentDetail.as_view(), name='detail'),
    path('create/', StudentCreate.as_view(), name='create'),
    path('delete/', StudentDelete.as_view(), name='delete'),
    # path('example/', CreateTodoAPIView.as_view(), name='user'),
]
