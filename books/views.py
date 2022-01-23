from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import isOwnerOrReadOnly

from .models import Book, Comment
from .serializers import BookSerializer, CommentSerializer

class BookListView(ListCreateAPIView):
    ''' View for /books endpoint GET/POST '''

    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class BookDetailView(RetrieveUpdateDestroyAPIView):
    ''' View for /books/id endpoint GET/PUT/PATCH/DELETE'''

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentListView(CreateAPIView):
    ''' View for /books/id/comments POST'''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentDetailView(DestroyAPIView):
    ''' View for /books/id/comments/commentId DELETE'''

    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer
    permission_classes = (isOwnerOrReadOnly, )
    