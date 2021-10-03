from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('register/', register, name='register'),
    path('login/', loginPage, name="login")

]