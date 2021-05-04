from django.urls import path
from cbvTest import views

urlpatterns = [
    path('', views.UserAddandShow.as_view(), name="add_and_show"),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name="delete_data"),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name="update_data"),
]
