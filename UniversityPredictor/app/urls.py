from django.urls import path
from . import views

urlpatterns = [
	path('', views.register,name="register"),
	path('login/', views.student_login,name="student_login"),
	path('dashboard/', views.dashboard,name="dashboard"),
	path('logout/', views.logout,name="logout"),
	path('admin_home/', views.admin_home,name="admin_home"),
	path('medical/', views.medical,name="medical"),
	path('agri_search/', views.agri_search,name="agri_search"),
	path('engineering_search/', views.engineering_search,name="engineering_search"),
	path('agri_colg_search/', views.agri_colg_search,name="agri_colg_search"),
	path('medical_search/', views.medical_search,name="medical_search"),
	
]
