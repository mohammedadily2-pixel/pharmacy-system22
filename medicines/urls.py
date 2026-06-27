from django.urls import path
from . import views

urlpatterns = [
    path('login/',    views.login_view,    name='login'),
    path('logout/',   views.logout_view,   name='logout'),
    path('dashboard/',          views.dashboard_view,    name='dashboard'),
    path('medicines/',          views.medicine_list,     name='medicine_list'),
    path('medicines/add/',      views.add_medicine,      name='add_medicine'),
    path('medicines/expired/',  views.expired_medicines, name='expired'),
    path('medicines/expiring/', views.expiring_soon,     name='expiring_soon'),
    path('medicines/delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('medicines/edit/<int:pk>/',   views.edit_medicine,   name='edit_medicine'),
]