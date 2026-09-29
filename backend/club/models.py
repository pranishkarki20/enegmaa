from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=40, default="COMMUNITY")
    starts_at = models.DateTimeField()
    venue = models.CharField(max_length=180, blank=True)
    registration_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["starts_at"]

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=180)
    summary = models.CharField(max_length=240)
    technology = models.CharField(max_length=120, blank=True)
    url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class MembershipInquiry(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
