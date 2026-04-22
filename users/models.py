from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('User photo',default='default.png', upload_to='user_images')

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'), ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    email_notifications = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old = Profile.objects.get(pk= self.pk)
                if old.img != self.img:
                    if old.img.name != 'default.png' and os.path.isfile(old.img.path):
                        os.remove(old.img.path)
            except Profile.DoesNotExist:
                pass
        super().save(*args, **kwargs)
        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)



    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

