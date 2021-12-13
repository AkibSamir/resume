from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/profile" )
    cv = models.FileField(upload_to="cv", blank=True, null=True, help_text="Download CV")

    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    is_keyskill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    institute = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio", default="images/work-img.jpg")
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="testimonial", default="images/user-img.jpg")

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog", default="images/work-img.jpg")
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



