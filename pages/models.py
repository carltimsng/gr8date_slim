from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# ----------------------------
# Existing models
# ----------------------------

class Profile(models.Model):
    user_id = models.IntegerField(unique=True, db_index=True)
    display_name = models.CharField(max_length=200, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    primary_image = models.ImageField(upload_to='profiles/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.display_name or 'User'} (#{self.user_id})"

    # ---- NEW helper methods ----
    def public_images(self):
        return self.images.filter(kind=ProfileImage.PUBLIC).order_by("position")

    def additional_images(self):
        return self.images.filter(kind=ProfileImage.ADDITIONAL).order_by("position")

    def private_images(self):
        return self.images.filter(kind=ProfileImage.PRIVATE).order_by("position")


class ProfileImage(models.Model):
    PUBLIC = 'public'
    ADDITIONAL = 'additional'
    PRIVATE = 'private'

    IMAGE_KIND_CHOICES = [
        (PUBLIC, 'Public'),
        (ADDITIONAL, 'Additional'),
        (PRIVATE, 'Private'),
    ]

    profile = models.ForeignKey(Profile, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/gallery/%Y/%m/%d/')
    kind = models.CharField(max_length=20, choices=IMAGE_KIND_CHOICES, default=ADDITIONAL)
    source_url = models.URLField(blank=True)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.profile_id}-{self.kind}-{self.position}"


# ----------------------------
# Blog models
# ----------------------------

User = get_user_model()

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        """Return posts that are published and past their publish_at date."""
        now = timezone.now()
        return self.filter(status='published', publish_at__lte=now)


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, help_text="URL slug (auto from title).")
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    category = models.CharField(max_length=80, blank=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish_at = models.DateTimeField(default=timezone.now, help_text="When this post becomes visible.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostQuerySet.as_manager()

    class Meta:
        ordering = ['-publish_at']

    def __str__(self):
        return self.title

