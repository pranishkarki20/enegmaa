from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Event, MembershipInquiry, Project
from .serializers import EventSerializer, MembershipInquirySerializer, ProjectSerializer

class EventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(is_published=True, starts_at__gte=timezone.now())

class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_published=True)

class MembershipSignup(APIView):
    def post(self, request):
        serializer = MembershipInquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inquiry, created = MembershipInquiry.objects.get_or_create(email=serializer.validated_data["email"])
        return Response({"message": "Thanks for your interest!", "created": created}, status=201 if created else 200)
