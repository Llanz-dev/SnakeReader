from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile

CATEGORIES_POSTS = (
    ('health','HEALTH'),
    ('sports', 'SPORTS'),
    ('finance','FINANCE'),
    ('technology','TECHNOLOGY'),
    ('fashion','FASHION'),
    ('travel','TRAVEL'),
    ('music','MUSIC'),
)

# Create your models here.
class Article(models.Model):
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)    
    title = models.CharField(max_length=80)
    category_choices = models.CharField(max_length=10, choices=CATEGORIES_POSTS, default='health')
    slug = models.SlugField(unique=True)
    intro = models.TextField(blank=False, null=True)
    body = RichTextUploadingField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    heading_img = models.ImageField(blank=True, upload_to='article_heading', default='article_heading/default.jpg')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)    
    