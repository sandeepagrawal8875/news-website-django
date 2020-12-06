from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import  Q

from .models import Blog, Contact
from django.urls import reverse_lazy

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class ContactView(CreateView):
    model = Contact
    fields = "__all__"
    template_name = 'blog/contact.html'
    success_url = reverse_lazy('list')

def blogListView(request):

    si = request.GET.get("si")
    if si == None:
        si = ""
        blog_p = Blog.objects.all().order_by('-id')
    else:
        blog_p = Blog.objects.filter(
            Q(course_name__icontains=si) | 
            Q(tags__icontains=si) | 
            Q(author__icontains=si) | 
            Q(categories__icontains=si)).order_by("-id")

    popular_blog = Blog.objects.all().order_by("-views")[:7]
    blog_tag = Blog.objects.all()

    tags = set()
    for x in blog_tag:
        tag_lst = x.tags.split(",")
        for i in tag_lst:
            if i not in tags:
                tags.add(i)

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_p, 5)
    try:
        blog_obj = paginator.page(page)
    except PageNotAnInteger:
        blog_obj = paginator.page(1)
    except EmptyPage:
        blog_obj = paginator.page(paginator.num_pages)

    context = {
        "blog_obj" : blog_obj,
        "popular_blog_obj" : popular_blog,
        "tags":tags,
    }
    return render(request, "blog/blog_list.html", context=context)


def tagsList(request, value):
    blog_p = Blog.objects.filter(
        Q(course_name__icontains=value) |
        Q(tags__icontains=value)
    ).order_by("-views")

    popular_blog = Blog.objects.all().order_by("-views")[:7]
    blog = Blog.objects.all()

    tags = set()
    for x in blog:
        tag_lst = x.tags.split(",")
        for i in tag_lst:
            if i not in tags:
                tags.add(i)

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_p, 5)
    try:
        blog_obj = paginator.page(page)
    except PageNotAnInteger:
        blog_obj = paginator.page(1)
    except EmptyPage:
        blog_obj = paginator.page(paginator.num_pages)

    context = {
        "blog_obj" : blog_obj,
        "popular_blog_obj" : popular_blog,
        "tags":tags,
    }
    return render(request, "blog/blog_list.html", context=context)


class BlogDetail(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog
    fields = ['course_name','author', 'categories','description', 'link','tags','picture']
    context_object_name = 'blog'
    # pk_url_kwarg = "post_id"

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.incrementViewCount()
        return item

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        popular_blog = Blog.objects.all().order_by("-views")[:5]
        blog = Blog.objects.all()

        tags = set()
        for x in blog:
            tag_lst = x.tags.split(",")
            for i in tag_lst:
                if i not in tags:
                    tags.add(i)

        data['tags'] = tags
        data['popular_blog_obj'] = popular_blog
        return data

class BlogDeleteView(DeleteView):
    template_name = 'blog/blog_delete_form.html'
    model = Blog
    success_url = reverse_lazy('list')
    
    

class BlogCreateView(CreateView):
    model = Blog
    fields = ['course_name','author', 'categories','description', 'link','tags','picture']
    success_url = reverse_lazy('list')
    template_name = 'blog/blog_create_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        popular_blog = Blog.objects.all().order_by("-views")[:5]
        blog = Blog.objects.all()

        tags = set()
        for x in blog:
            tag_lst = x.tags.split(",")
            for i in tag_lst:
                if i not in tags:
                    tags.add(i)

        data['tags'] = tags
        data['popular_blog_obj'] = popular_blog
        return data

class BlogUpdate(UpdateView):
    model = Blog
    template_name = 'blog/blog_update_form.html'
    fields = ['course_name','author', 'categories','description', 'link','tags','picture']
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        popular_blog = Blog.objects.all().order_by("-views")[:5]
        blog = Blog.objects.all()

        tags = set()
        for x in blog:
            tag_lst = x.tags.split(",")
            for i in tag_lst:
                if i not in tags:
                    tags.add(i)

        data['tags'] = tags
        data['popular_blog_obj'] = popular_blog
        return data

