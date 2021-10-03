from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task-detail"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('register/', register, name='register'),
    path('login/', loginPage, name="login")

]