from rest_framework import generics
from .models import Agent, Client, Text, Track, Ransom
from .serializers import AgentSerializer, ClientSerializer, TextSerializer, TrackSerializer, RansomSerializer

class AgentViewSet(generics.ListCreateAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()

    def get_queryset(self, *args, **kwargs):
        id = self.request.query_params.get('id')
        code = self.request.query_params.get('code')
        if id is not None:
            data = Agent.objects.filter(tg_id=id)
        elif code is not None:
            data = Agent.objects.filter(code=code)
        else:
            data = Agent.objects.all()
        return data


class ClientViewSet(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self, *args, **kwargs):
        code = self.request.query_params.get('code')
        if id is not None:
            data = Client.objects.filter(code=code)
        else:
            data = Client.objects.all()
        return data


class TextViewSet(generics.ListAPIView):
    serializer_class = TextSerializer
    queryset = Text.objects.all().order_by("id")


class TrackViewSet(generics.CreateAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()

class RansomViewSet(generics.CreateAPIView):
    serializer_class = RansomSerializer
    queryset = Ransom.objects.all()