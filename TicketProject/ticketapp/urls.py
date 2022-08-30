from django.urls import path
from . import views

urlpatterns = [
    path('user_reg/',views.user_registration_view,name='user_reg'),
    path('user_log/',views.user_login_view,name='login'),
    path('home/', views.ticket_generation_view,name='home'),
    path('admin_home/',views.admin_view,name='admin_home'),
    path('logout/',views.user_logout,name='logout'),
    path('user_update/<int:id>/',views.user_update_view,name='update_user'),
    path('delete_user/<int:id>/',views.user_delete_view,name='delete_user'),
    path('admin_update/<int:id>/',views.admin_update_view,name='update_admin'),
    path('delete_admin/<int:id>/',views.admin_delete_view,name='delete_admin'),
    path('admin_tik/',views.admin_ticket_resolve_view,name='admin_up'),
]