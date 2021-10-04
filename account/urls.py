from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task-detail"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name="task-delete"),
    path('register/', register, name='register'),
    path('register-page/', registerPage.as_view(), name="register-page"),
    path('login/', loginPage.as_view(), name="login"),
    path('logout/', logoutPage.as_view(), name='logout'),

]