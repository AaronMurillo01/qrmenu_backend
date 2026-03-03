from rest_framework import permissions
from . import models

class IsOwnerOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
        return True
    return obj.owner == request.user

class PlaceOwnerOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
        return True
    return obj.place.owner == request.user

  def has_permission(self, request, view):
    if request.method == "POST":
      place_id = request.data.get("place")
      if place_id is None:
        return False
      return models.Place.objects.filter(pk=place_id, owner_id=request.user.id).exists()
    return True