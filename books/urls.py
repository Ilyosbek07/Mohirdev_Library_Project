from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from books.views import BookCreateAPIView, BookListAPIView, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, \
    BookViewset

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    # path('', BookListCreateAPIView.as_view()),
    # path('delete/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),

    # Function APIView
    # path('books/', BookListAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
]

urlpatterns = urlpatterns + router.urls
