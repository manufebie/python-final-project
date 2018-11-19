from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    # Retrieve list of article objects
    model = Article


class MyArticleListView(LoginRequiredMixin, ListView):
    # Retrieve list of article objects owned by user
    model = Article
    template_name = 'blog/my_articles_list.html'

    def get_queryset(self):
        # filter this list for the logged in user
        return Article.objects.filter(user=self.request.user)


class ArticleDetailView(DetailView):
    # retrieve single article object
    model = Article


class ArticleCreateView(CreateView):
    # create article object
    model = Article
    fields = ['title', 'subtitle', 'slug', 'body', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    # update existing article object
    model = Article
    fields = ['title', 'subtitle', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    # delete article object
    model = Article
    success_url = reverse_lazy('account:article_list')
    #success_url = reverse_lazy('')

