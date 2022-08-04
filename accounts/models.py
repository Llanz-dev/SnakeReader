from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    province = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
    user_slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.user.first_name)
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    