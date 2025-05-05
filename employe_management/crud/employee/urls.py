from django.urls import path
from . import views
urlpatterns = [
    path('',views.employee_list,name='list'),
    path('create/',views.create_employee,name='create'),
    path('update/<int:pk>/',views.employee_update,name='update'),
    path('delete/<int:pk>/',views.delete_employee,name='delete'),
]
