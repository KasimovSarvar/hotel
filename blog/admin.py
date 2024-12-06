from django.contrib import admin
from .models import Contact, Category, Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "created_at", "category")
    list_display_links = ("id", "title")
    list_filter = ("created_at", "is_published")

    class Meta:
        model = Post

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",  "created_at", "message")
    list_display_links = ("name", "email")
    list_filter = ("created_at",)

    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
