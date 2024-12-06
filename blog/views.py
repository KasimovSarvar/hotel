from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Post, Contact, Comment, Category, Tag
from django.core.paginator import Paginator
import requests
from django.conf import settings

def home_view(request):
    posts = Post.objects.filter(is_published=True)
    data = request.GET
    page_number = int(data.get('page', 1))
    paginator = Paginator(posts, 2)
    all_page = Post.objects.all()

    d = {
        'posts': paginator.get_page(page_number),
         "all_page":all_page

    }
    return render(request, 'index.html', context=d)


def blog_view(request):
    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts,
    }
    return render(request, 'base.html', context=d)


def home_detail_view(request, pk):
    post = Post.objects.filter(id=pk, is_published=True).first()
    comments = Comment.objects.filter(post=post)
    if post:
        post.view_count += 1
        post.save(update_fields=['view_count'])

    d = {
        'post': post,
        'comments': comments,
    }

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        website = data.get('website')
        message = data.get('message')
        obj = Comment.objects.create(post=post, name=name, email=email, website=website, message=message)
        obj.save()
        post.comment_count += 1
        post.save(update_fields=['comment_count'])
        return redirect(f"/home/{pk}")

    return render(request, 'blog-single.html', context=d)


def about_view(request):
    posts = Post.objects.filter(is_published=True)

    d = {
        'posts': posts,

    }
    return render(request, 'about.html', context=d)


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('gmail')
        message = data.get('message')

        obj = Contact.objects.create(name=name, phone=phone, email=email, message=message)
        obj.save()
        res = requests.get(settings.BASE_URL.format(settings.TELEGRAM_BOT_TOKEN, settings.TELEGRAM_CHANNEL_ID,
                                            f"name: {name} \nemail: {email} \nphone: {phone} \nmessage:{message}"))
        print(res)

        return redirect('/contact')

    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts,
    }

    return render(request, 'contact.html', context=d)


def category_view(request, pk):
    posts = Post.objects.filter(category_id=pk, is_published=True)
    cat = Category.objects.filter(id=pk).first()

    data = request.GET
    page_number = int(data.get('page', 1))
    paginator = Paginator(posts, 1)
    all_page = Post.objects.all()

    d = {
        'category': cat,
        'posts': paginator.get_page(page_number),
        "all_page": all_page

    }
    return render(request, 'category.html', context=d)


def tag_view(request, pk):
    posts = Post.objects.filter(tag__id=pk)
    tags = Tag.objects.filter(id=pk).first()

    data = request.GET
    page_number = int(data.get('page', 1))
    paginator = Paginator(posts, 1)
    all_page = Post.objects.all()

    d = {
        'tag': tags,
        'posts': paginator.get_page(page_number),
        "all_page": all_page
    }

    return render(request, 'tag_page.html', context=d)


def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('query')
        filter_ = Q(title__icontains=search_query)
        filter_ |= Q(description__icontains=search_query)
        posts = Post.objects.filter(filter_)

        data = request.GET
        page_number = int(data.get('page', 1))
        paginator = Paginator(posts, 12)
        all_page = Post.objects.all()


        d = {
            'posts': paginator.get_page(page_number),
            "all_page": all_page
        }

        return render(request, 'search.html', d)

