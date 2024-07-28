from django.urls import path
from .views import AlertCreateAPIView, AlertListAPIView, AlertDeleteAPIView

urlpatterns = [
    path('create/', AlertCreateAPIView.as_view(), name='alert-create'),
    path('delete/<int:pk>/', AlertDeleteAPIView.as_view(), name='alert-delete'),
    path('', AlertListAPIView.as_view(), name='alert-list'),
]