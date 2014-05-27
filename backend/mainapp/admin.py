from django.contrib import admin
from django.contrib.contenttypes import generic
from models import MediaFile, ExtraUserInfo, Equipement, ResearchTopic, Announcement
# Register your models here.
class MediaFileInline(generic.GenericTabularInline):
  model = MediaFile
  ct_fk_field = "owner_id"
  ct_field = "generic_owner"

class EquipementAdmin(admin.ModelAdmin):
  inlines = [
    MediaFileInline,
  ]

class ExtraUserInfoAdmin(admin.ModelAdmin):
  inlines = [
    MediaFileInline,
  ]

class ResearchTopicAdmin(admin.ModelAdmin):
  inlines = [
    MediaFileInline,
  ]

class AnnouncementAdmin(admin.ModelAdmin):
  inlines = [
    MediaFileInline,
  ]

admin.site.register(MediaFile)
admin.site.register(ExtraUserInfo, ExtraUserInfoAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(ResearchTopic, ResearchTopicAdmin)
admin.site.register(Announcement, AnnouncementAdmin)

