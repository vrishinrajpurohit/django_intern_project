from django.urls import path
from .views import BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, BlogPostDetailView, BlogPostListView
from django.views.generic import TemplateView

urlpatterns = [
    path('blogpost/new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blogpost/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blogpost/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blogs/', BlogPostListView.as_view(), name='blogpost_list'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
