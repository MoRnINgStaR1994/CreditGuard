from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Card
from .serializers import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title']
    ordering_fields = ['created_at']
    search_fields = ['title']

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
