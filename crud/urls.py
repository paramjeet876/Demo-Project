from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserList.as_view(), name='user-list'),  # GET to list users, POST to create a new user
    path('api/users/create/', views.UserCreate.as_view(), name='user-create'),  # POST to create a new user
    path('api/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),  # GET a user by ID
    path('api/users/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),  # PUT to update a user
    path('api/users/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),  # DELETE to delete a user
]
