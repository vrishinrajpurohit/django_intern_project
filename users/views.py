from .models import CustomUserModel
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomHostUserCreationForm,CustomHostUserChangeForm
from django.urls import reverse_lazy
from blogs.models import BlogPost
# Create your views here.

class Signupview(CreateView):
    form_class = CustomHostUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'ProfileUpdate.html'
    model = CustomUserModel
    form_class = CustomHostUserChangeForm

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse_lazy('hosthome')

class ProfileDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "ProfileDelete.html"
    model = CustomUserModel

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse_lazy('home')
class ProfileView(TemplateView):
    template_name = 'HostHome.html'

class ProfileBlogView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'doctorblogs.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)