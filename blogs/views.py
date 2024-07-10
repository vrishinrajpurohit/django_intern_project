from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import BlogPost, Category

class BlogPostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BlogPost
    fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
    template_name = 'blogpost_form.html'
    success_url = reverse_lazy('hosthome')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_doctor

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
    template_name = 'blogpost_form.html'
    success_url = reverse_lazy('hosthome')

    def test_func(self):
        blog_post = self.get_object()
        return self.request.user == blog_post.author

class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('hosthome')

    def test_func(self):
        blog_post = self.get_object()
        return self.request.user == blog_post.author

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'

class BlogPostListView(LoginRequiredMixin,ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_draft=False)
