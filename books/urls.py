from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    CommentListView,
    CommentDetailView
)

urlpatterns = [
    path('', BookListView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('<int:pk>/comments/', CommentListView.as_view()),
    path('<int:book_pk>/comments/<int:pk>/', CommentDetailView.as_view())
]
