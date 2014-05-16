from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
# Create your models here.

class MediaFile(models.Model):
  name = models.CharField(max_length=500)
  media_file = models.FileField(max_length=1000, upload_to='/')
  generic_owner = models.ForeignKey(ContentType)
  owner_id = models.PositiveIntegerField()
  owner_object = generic.GenericForeignKey('generic_owner', 'owner_id')

class ExtraUserInfo(models.Model):
  user = models.OneToOneField(User)
  brief = models.TextField()
  media_files = generic.GenericRelation(MediaFile)

class Equipement(models.Model):
  name = models.CharField(max_length=500)
  description = models.TextField()
  media_files = generic.GenericRelation(MediaFile)

class ResearchTopic(models.Model):
  title = models.CharField(max_length=500)
  description = models.TextField()
  supervisor = models.ForeignKey(User, related_name="supervised_topics")
  researchers = models.ManyToManyField(User, related_name="working_topics")
  media_files = generic.GenericRelation(MediaFile)

class Announcement(models.Model):
  title = models.CharField(max_length=500)
  description = models.TextField()
  media_files = generic.GenericRelation(MediaFile)
  related_members = models.ManyToManyField(User)
