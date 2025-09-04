from django.contrib import admin
from .models import Profile, ProfileImage, BlogPost

class ProfileImageInline(admin.TabularInline):
    model = ProfileImage
    extra = 0
    fields = ("image", "kind", "position", "source_url")
    ordering = ("position", "id")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "age", "gender", "location", "created_at")
    search_fields = ("display_name", "location", "bio")
    list_filter = ("gender",)
    inlines = [ProfileImageInline]

@admin.register(ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ("profile", "kind", "position")
    list_filter = ("kind",)
    search_fields = ("profile__display_name",)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "publish_at", "author")
    list_filter = ("status", "category")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}

