from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RestaurantCreateForm
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# from validate_email import validate_email


class RestaurantListView(ListView):
    template_name = 'restaurants/restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 6

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(location__icontains=search_query))

        return queryset
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('unlike')
        post_id2 = request.POST.get('like')
        if post_id is not None:
            post = get_object_or_404(Restaurant, id=post_id)
            post.likes.remove(request.user)
        if post_id2 is not None:
            post_id2 = request.POST.get('like')
            post = get_object_or_404(Restaurant, id=post_id2)
            post.likes.add(request.user)
        return redirect('home')


class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        comment = request.POST.get('comment')
        c_slug = request.POST.get('slug')
        if comment:
            if c_slug:
                post = get_object_or_404(Restaurant, slug=c_slug)
                comment = Comment.objects.create(
                    user=request.user, post=post, text=comment)
                comment.save()
                return redirect('detail', c_slug)
        return redirect('detail', c_slug)


class RestaurantCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'restaurants/restaurant_form.html'
    form_class = RestaurantCreateForm
    success_url = reverse_lazy('my_posts')
    success_message = "Post Created Successfully"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class RestaurantUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = RestaurantCreateForm
    template_name = 'restaurants/restaurant_form.html'
    success_url = reverse_lazy('my_posts')
    success_message = "Post Updated Successfully"

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)


class RestaurantDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    success_url = reverse_lazy('my_posts')
    success_message = "Post Deleted Successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)


class MyPostView(LoginRequiredMixin, ListView):
    template_name = 'restaurants/my_posts.html'

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)
    
#=============================================================================================
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def custom_logout(request):
    # Perform any additional logic before logout if needed
    logout(request)
    messages.success(request, 'You have been successfully logged out.')  # Optional: Display a success message
    return redirect('home')  # Redirect to the home page or any other desired page  

