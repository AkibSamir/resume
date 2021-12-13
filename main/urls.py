from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blog_detail, name='blog-detail'),
    path('portfolio/', views.Portfolios, name="portfolio"),
    path('portfolio-detail/', views.Portfolio_detail, name="portfolio-detail"),
    path('contact/', views.Contact, name='contact'),
]