# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Case(models.Model):
    title = models.CharField(max_length = 255)  # The title of the news article
    pub_date = models.DateTimeField(auto_now_add = True, verbose_name= "Published date")  # The publication date
    content = RichTextField(config_name='awesome_ckeditor') # The full text content of the news article
    source = models.URLField(max_length=200, blank=True, null = True)  # URL to the original source
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # An image for the article

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']  # Orders the articles from most to least recent



class Service(models.Model):
    title = models.CharField(max_length = 255)  # The title of the news article
    pub_date = models.DateTimeField(auto_now_add = True, verbose_name= "Published date")  # The publication date
    content = RichTextField(config_name='awesome_ckeditor') # The full text content of the news article
    source = models.URLField(max_length=200, blank=True, null = True)  # URL to the original source
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # An image for the article

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']  # Orders the articles from most to least recent


class News(models.Model):
    title = models.CharField(max_length = 255)  # The title of the news article
    author = models.CharField(max_length=100,blank=True, null = True)  # The author of the news article
    pub_date = models.DateTimeField(auto_now_add = True, verbose_name= "Published date")  # The publication date
    content = RichTextField(config_name='awesome_ckeditor') # The full text content of the news article
 
    source = models.URLField(max_length=200, blank=True, null = True)  # URL to the original source
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # An image for the article

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']  # Orders the articles from most to least recent
        


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null = True, blank = True)
    phone_number = models.CharField(max_length=17, blank=True)  # validators should be a list
    message = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact :L e:\freelance\paprica\v01\posts\forms.py{self.name}"

    class Meta:
        ordering = ['-created_at']
