from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path("login/", views.user_login, name="login"),
    path('edit/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path("register/", views.register, name="register"),
]
urlpatterns += [
    path("logout/", views.user_logout, name="logout"),
]
