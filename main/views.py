from types import CodeType
from django.shortcuts import render, redirect
from .models import Profile, Skills, Certificate, Portfolio, Testimonial, Blog, Contact
from .forms import ContactForm

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    skills = Skills.objects.all()
    certificates = Certificate.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()
    # if request.method == "POST":
    #     profiles = Profile(request.POST, request.FILES)

    context = {
        'profiles':profiles,
        'skills':skills,
        'certificates':certificates,
        'portfolios':portfolios,
        'testimonials':testimonials,
        'blogs':blogs,
    }
    return render(request, 'index.html', context=context)


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'blog.html', context=context)

def blog_detail(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'blog-detail.html', context=context)

def Portfolios(request):
    portfolios = Portfolio.objects.all()
    context={
        'portfolios':portfolios,
    }
    return render(request, 'portfolio.html', context=context)

def Portfolio_detail(request):
    portfolios = Portfolio.objects.all()
    context={
        'portfolios':portfolios,
    }
    return render(request, 'portfolio-detail.html', context=context)

def Contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    context = {
        'form':form,
    }
    return render(request, 'contact.html', context=context)
