from django.urls import path
from .views import BlogCreateView, BlogDetail, blogListView, BlogUpdate, BlogDeleteView, tagsList, AboutView,ContactView

urlpatterns = [
    path('', blogListView, name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('tag/<str:value>/', tagsList, name="tag"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact")
]
