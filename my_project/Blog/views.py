from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import ArticleForm
from .models import Article


# Create your views here.


def home_view(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            print(form)
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("blog:blog-home"))
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "registration/register.html", context)


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    queryset = Article.objects.all()


def article_list_view(request):
    my_articles = Article.objects.all()
    context = {
        "articles": my_articles,
    }
    return render(request, "article_list.html", context)


class ArticleCreateView(CreateView):
    template_name = "article_create.html"
    queryset = Article.objects.all()
    form_class = ArticleForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def create_view(request):
    if request.method == "POST":
        my_form = ArticleForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return HttpResponseRedirect(reverse("blog:blog-list"))
    else:
        my_form = ArticleForm()
    context = {
        "form": my_form,
    }
    return render(request, "article_create.html", context)


class ArticleDetailView(DetailView):
    template_name = "article_detail.html"

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get("id"))


class ArticleUpdateView(UpdateView):
    template_name = "article_create.html"
    queryset = Article.objects.all()
    form_class = ArticleForm

    def get_object(self, queryset=None):
        return get_object_or_404(Article, id=self.kwargs.get("id"))

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def article_detail_view(request, my_id):
    article = Article.objects.get(id=my_id)
    context = {
        "article": article,
    }
    return render(request, "article_detail_view.html", context)


class ArticleDeleteView(DeleteView):
    template_name = "article_delete.html"

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get("id"))

    def get_success_url(self):
        return reverse("blog:blog-list")
