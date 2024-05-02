from django.urls import path
from .views import AgentViewSet, ClientViewSet, TextViewSet, TrackViewSet, RansomViewSet, ButtonViewSet

urlpatterns = [
    path('agent/', AgentViewSet.as_view()),
    path('client/', ClientViewSet.as_view()),
    path('text/', TextViewSet.as_view()),
    path('button/', ButtonViewSet.as_view()),
    path('track/', TrackViewSet.as_view()),
    path('ransom/', RansomViewSet.as_view()),
]