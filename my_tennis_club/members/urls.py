from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),  # URL for viewing all members
    path('members/details/<int:id>/', views.details, name='details'),  # Nested URL for viewing member details
]
