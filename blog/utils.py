from .models import Category, Tag, Post

def get_category(request):

    d = {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'sidebar': Post.objects.filter(is_published=True).order_by('-view_count')[:3],
        'latest': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
        'comment': Post.objects.filter(is_published=True).order_by('-comment_count')[:3],
    }
    return d