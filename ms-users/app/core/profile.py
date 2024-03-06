from django.db import models


class Profile(models.Model):
    """Database model for users"""
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/profiles/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sn_facebook = models.CharField(max_length=255, blank=True)
    sn_twitter = models.CharField(max_length=255, blank=True)
    sn_linkedin = models.CharField(max_length=255, blank=True)
    sn_instagram = models.CharField(max_length=255, blank=True)
    sn_github = models.CharField(max_length=255, blank=True)
    sn_youtube = models.CharField(max_length=255, blank=True)
    sn_website = models.CharField(max_length=255, blank=True)
