from django.contrib import admin
from .models import Event, MembershipInquiry, Project

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(MembershipInquiry)
