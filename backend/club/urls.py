from django.urls import path
from .views import EventList, MembershipSignup, ProjectList

urlpatterns = [path("events/", EventList.as_view(), name="events"), path("projects/", ProjectList.as_view(), name="projects"), path("join/", MembershipSignup.as_view(), name="join")]
