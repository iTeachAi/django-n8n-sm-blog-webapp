from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .services import generate_post
from .models import Post
from .forms import PostForm


class HomeView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)
           posts = Post.objects.all()
           context['posts'] = posts
           return context

        

class CreatePostView(CreateView):
    template_name = "app/upload_post.html"
    model = Post
    form_class = PostForm
    def get_success_url(self):
        return reverse(
            "post_details",
            kwargs = {"id": self.object.id},
        )

    def form_valid(self, form):
        response = super().form_valid(form)

        try:
            result = generate_post(
                image=self.object.image,
                name=self.object.name,
                date=self.object.date,
                lesson = self.object.lesson,
                facebook=self.object.post_to_facebook,
                instagram=self.object.post_to_instagram,
                linkedin=self.object.post_to_linkedin,
                tiktok=self.object.post_to_tiktok,
                imagewithpost=self.object.request_image,
            )

            # Save the returned JSON
            self.object.generated_content = result
            self.object.generation_status = "completed"
            self.object.generation_error = ""
        
            self.object.save(
                update_fields = [
                    "generated_content",
                    "generation_status",
                    "generation_error",
                ]
            )

            messages.success(
                self.request,
                "The post content was generated successfully",
            )
        except Exception as error:
            self.object.generation_status = "failed"
            self.object.generation_error = str(error)

            self.object.save(
                update_fields = [
                    "generation_status",
                    "generation_error",
                ]
            )
        return response
   

class DetailedPostView(DetailView):
    model = Post
    pk_url_kwarg = "id"
    template_name = 'app/post_details.html'
    context_object_name = "post"

class DeletePostView(DeleteView):
    model=Post
    pk_url_kwarg = 'id'
    template_name = 'app/delete_post.html'
    success_url = reverse_lazy('home')