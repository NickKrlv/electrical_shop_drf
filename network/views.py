from rest_framework import viewsets, permissions
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from rest_framework import filters


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']
