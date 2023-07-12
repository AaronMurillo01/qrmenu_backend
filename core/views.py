from rest_framework import generics
from . import models, serializers

# Create your views here.
class PlaceList(generics.ListCreateAPIView):
    serializers_class = serializers.PlaceSerializer
    
    def get_queryset(self):
        return models.Place.object.filter(owner_id=self.request.user.id)

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)