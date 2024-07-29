from django.db.models.query import QuerySet
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')


class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact= self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post
    
    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            if self.object.group and not self.object.user.groups.filter(pk=self.object.group.pk).exists():
                raise ValidationError("You are not a member of this group")
            self.object.save()
            return redirect('posts:all')
        except ValidationError as e:
            storage = messages.get_messages(self.request)
            for message in storage:
                pass  # Iterating through messages clears them
            messages.error(self.request, str(e), 'group_not_joined')
            return super().form_invalid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
    