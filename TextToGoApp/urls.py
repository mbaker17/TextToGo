from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('pages/register/', views.register, name='register'),
    path('pages/login/', views.loginPage, name='login'),
    path('pages/logout/', views.logoutUser, name='logout'),

    path('pages/selectDate/', views.selectDate, name='select_date'),
    path('pages/createOrder/', views.createOrderObject, name='create_orderobject'),
    path('pages/schedule/', views.schedule, name='schedule'),

    path('editOrder/<str:pk>/',views.editOrder, name='editOrder'),
    path('deleteOrder/<str:pk>/',views.deleteOrder, name='deleteOrder'),
]