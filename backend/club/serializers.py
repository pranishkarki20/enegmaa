from rest_framework import serializers
from .models import Event, MembershipInquiry, Project

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "description", "category", "starts_at", "venue", "registration_url"]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "summary", "technology", "url"]

class MembershipInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipInquiry
        fields = ["email"]
