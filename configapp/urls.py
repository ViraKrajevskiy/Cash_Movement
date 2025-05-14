from django.urls import path
from configapp.views import *

urlpatterns = [
    path('', dds_list_view, name='dds_list'),
    path('create/', dds_create_view, name='dds_create'),
    path('edit/<int:pk>/', dds_edit_view, name='dds_edit'),
    path('delete/<int:pk>/', dds_delete_view, name='dds_delete'),

    # Status URLs
    path('statuses/', status_list_view, name='status_list'),
    path('status/create/', status_create_view, name='status_create'),
    path('status/edit/<int:pk>/', status_edit_view, name='status_edit'),
    path('status/delete/<int:pk>/', status_delete_view, name='status_delete'),

    # Type URLs
    path('types/', type_list_view, name='type_list'),
    path('type/create/', type_create_view, name='type_create'),
    path('type/edit/<int:pk>/', type_edit_view, name='type_edit'),
    path('type/delete/<int:pk>/', type_delete_view, name='type_delete'),

    # Category URLs
    path('categories/', category_list_view, name='category_list'),
    path('category/create/', category_create_view, name='category_create'),
    path('category/edit/<int:pk>/', category_edit_view, name='category_edit'),
    path('category/delete/<int:pk>/', category_delete_view, name='category_delete'),

    # Subcategory URLs
    path('subcategories/', subcategory_list_view, name='subcategory_list'),
    path('subcategory/create/', subcategory_create_view, name='subcategory_create'),
    path('subcategory/edit/<int:pk>/', subcategory_edit_view, name='subcategory_edit'),
    path('subcategory/delete/<int:pk>/', subcategory_delete_view, name='subcategory_delete'),

]

