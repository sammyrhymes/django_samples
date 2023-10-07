from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Blogger
from django.db.models import Count

# Create your views here.
def feed(request):
    blogs = Blog.objects.select_related('blogger').order_by("-pub_date")
    blog_data = []
    for blog in blogs:
        blog_data.append({
            "blog_id":blog.id,
            "title" : blog.title,
            "body":blog.body,
            "pub_date":blog.pub_date,
            "blogger": blog.blogger.name,
            "blogger_id":blog.blogger.id
        })
    context = {
        "title": "feed",
        "blog_data":blog_data
    }
    return render(request, "blog/index.html",context)

def article(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    ranks = Blogger.objects.annotate(blog_count = Count('blog')).order_by('-blog_count')[:5]
    context = {
        "blog":blog,
        "title": "blog",
        "ranks": ranks
    }
    return render(request, "blog/blog.html", context)


def writer(request, blogger_id):
    writer = Blogger.objects.get(pk = blogger_id)
    title = "writer"
    context = {
        "writer":writer,
        "title": title
    }
    return render(request, 'blog/writer.html', context)