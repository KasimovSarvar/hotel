from django import template
from blog.models import Tag

register = template.Library()

@register.simple_tag
def get_categories():
    return Tag.objects.all()