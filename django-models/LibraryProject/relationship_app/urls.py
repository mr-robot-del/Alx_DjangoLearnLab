from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
