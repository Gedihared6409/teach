from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('homy',views.homy, name = 'homy'),
    path('emloyee-register/',views.employee_register.as_view(),name='employeeregister'),
    path('manager-register/',views.manager_register.as_view(),name='managerregister'),
    path('procurementmanager-register/',views.procmanager_register.as_view(),name='procurementmanagerregister'),
   
    path('',views.home,name = 'welcome'),
    path('homee',views.homee,name = 'homee'),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('create_customer_order/<str:pk>/', views.create_customer_order, name="create_customer_order"),
    path('create_teacher_order/', views.create_teacher_order, name="create_teacher_order"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('register/', views.registerPage, name = 'register'),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name = "user-page"),
    path('teacher/', views.teacherPage, name = "teacher"),
    path('account/', views.accountSettings, name="account"),
    path('repairforms/', views.repairassets, name ='repairform'),
]