from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('logout', views.logout,name='logout'),
    path('editProfile', views.editProfile,name='EditProfile'),
    path('createTable',views.creatTable,name="createTable"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup',views.signup,name="signup"),
    path('forgotPassword',views.forgotPassword,name="forgotPassword"),
    path('getTable', views.getTable, name="getTable"),
    path('modifyrow', views.modifyrow, name="modifyrow"),
    path('deleteRow', views.deleteRow, name="deleteRow"),
    path('addColumn', views.addColumn, name="addColumn"),
    path('deleteColumn', views.deleteColumn, name='deleteColumn'),
    path('EditColumn', views.EditColumn, name='EditColumn'),
    path('getExperts', views.getExperts, name='getExperts'),
    path('sendemail', views.sendemail, name='sendemail'),
    path('getFields', views.getFields,name='getFields'),
    path('createExpert', views.createExpert,name='createExpert'),
    
]