from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def post_count(self):
        return self.posts.count()


class Tag(models.Model):
    name = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="posts")
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    image1 = models.ImageField(upload_to="posts/", blank=True, null=True)
    image2 = models.ImageField(upload_to="posts/", blank=True, null=True)

    description = RichTextField(blank=True, null=True)

    is_published = models.BooleanField(default=False)

    comment_count = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def comment_count(self):
    #     return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
