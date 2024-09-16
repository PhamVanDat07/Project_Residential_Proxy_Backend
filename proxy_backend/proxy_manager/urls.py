from django.urls import path
from . import views  # Import các view từ views.py

urlpatterns = [
    path('', views.home, name='home'),  # Đường dẫn cho trang chủ
    path('about/', views.about, name='about'),  # Đường dẫn cho trang "About"
]
