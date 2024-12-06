from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve

from .views import home_view, home_detail_view, about_view, contact_view, category_view, tag_view, search_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('home/<int:pk>/', home_detail_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('category/<int:pk>/', category_view),
    path('tag/<int:pk>/', tag_view),
    path('search/', search_view),

]

urlpatterns += static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)