from django.urls import path
from fbvTest import views

urlpatterns = [
    path('', views.add_show, name="addandshow"),
    path('delete/<int:pk>/', views.delete_data, name="deletedata"),
    path('update/<int:pk>/', views.update_data, name="updatedata"),
]
