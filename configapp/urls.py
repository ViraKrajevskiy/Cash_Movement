from django.urls import path
from configapp.views import dds_list_view, dds_delete_view, dds_edit_view

urlpatterns = [
    path('', dds_list_view, name='dds_list'),
    path('edit/<int:pk>/', dds_edit_view, name='dds_edit'),
    path('delete/<int:pk>/', dds_delete_view, name='dds_delete'),
]
