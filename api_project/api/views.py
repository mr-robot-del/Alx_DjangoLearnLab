from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        Customize permissions: AllowAnyone for GET, IsAuthenticated for POST/PUT,
        IsAdminUser for DELETE.
        """
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        elif self.action == 'destroy':
            return [IsAdminUser()]
        return [IsAuthenticated()]
