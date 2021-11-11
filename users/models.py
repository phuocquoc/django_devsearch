from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(
        blank=True, null=True, upload_to='profiles/', default='profiles/default.jpg')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_fb = models.CharField(max_length=200, blank=True, null=True)
    social_yt = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


def creatProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        subject = 'Welcom to DevSearch'
        message = 'We are glad you are here'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def deleleUser(sender, instance, **kwargs):
    print('Delete User')


post_save.connect(creatProfile, sender=User)
post_delete.connect(deleleUser, sender=Profile)
